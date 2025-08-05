from mcp.server.fastmcp import FastMCP
import json
import os

# Create the MCP server
mcp = FastMCP(app_name="Student Support Agent")


# --------------------
# Load Mock Course Data
# --------------------
file_path = os.path.join(os.path.dirname(__file__), "dataset", "mock_course_data.json")

with open(file_path, "r") as f:
    db = json.load(f)

courses = db["courses"]
instructors = db["instructors"]

# --------------------
# Utility Functions
# --------------------
def find_course(course_id):
    return next((c for c in courses if c["course_id"] == course_id), None)

def find_instructor(instructor_id):
    return next((i for i in instructors if i["instructor_id"] == instructor_id), None)

# --------------------
# Course Information Tools
# --------------------

@mcp.tool()
def get_course_details(course_id: str) -> dict:
    """Retrieve course description, objectives, prerequisites"""
    course = find_course(course_id)
    if not course:
        return {"error": "Course not found."}
    return {
        "title": course["title"],
        "description": course["description"],
        "objectives": course["objectives"],
        "prerequisites": course["prerequisites"]
    }

@mcp.tool()
def get_course_schedule(course_id: str) -> dict:
    """Access class timings, duration, session dates"""
    course = find_course(course_id)
    if not course:
        return {"error": "Course not found."}
    return course["schedule"]

@mcp.tool()
def get_course_syllabus(course_id: str) -> list:
    """Fetch detailed curriculum and learning modules"""
    course = find_course(course_id)
    if not course:
        return [{"error": "Course not found."}]
    return course["syllabus"]

@mcp.tool()
def get_course_pricing(course_id: str) -> dict:
    """Show fees, discounts, payment plans"""
    course = find_course(course_id)
    if not course:
        return {"error": "Course not found."}
    return course["pricing"]

@mcp.tool()
def search_courses(query: str = "", min_duration_weeks: int = 0) -> list:
    """Help students find relevant courses"""
    results = []
    for course in courses:
        title_match = query.lower() in course["title"].lower()
        if title_match:
            try:
                weeks = int(course["schedule"]["duration"].split()[0])
                if weeks < min_duration_weeks:
                    continue
            except:
                continue
            results.append({
                "course_id": course["course_id"],
                "title": course["title"],
                "description": course["description"]
            })
    return results

@mcp.tool()
def get_instructor_info(instructor_id: str) -> dict:
    """Provide teacher profiles and contact details"""
    instructor = find_instructor(instructor_id)
    if not instructor:
        return {"error": "Instructor not found."}
    return {
        "name": instructor["name"],
        "bio": instructor["bio"],
        "contact": instructor["contact"]
    }

# --------------------
# Dynamic Resources (optional)
# --------------------

@mcp.resource("course://{course_id}")
def course_summary(course_id: str) -> str:
    course = find_course(course_id)
    if course:
        return f"Course: {course['title']} - {course['description']}"
    return "Course not found."

@mcp.prompt()
def course_prompt(course_id: str) -> str:
    course = find_course(course_id)
    if course:
        return f"Generate a student-friendly summary for the course '{course['title']}'."
    return "Invalid course."

# --------------------
# Start the Server
# --------------------

if __name__ == "__main__":
    mcp.run()
