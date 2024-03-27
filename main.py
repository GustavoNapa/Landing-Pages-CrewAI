from crewai import Agent, Crew, Task

from tools.file_tools import FileTools
from tools.search_tools import SearchTools

from tools.cli_use_tools import execute_command
from tools.interpreter_open_ai import interpret_code_with_openai

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

file_tools = FileTools()
search_tools = SearchTools()

# Create a new agent
senior_developer = Agent(
    role="Senior Software Engineer",
    goal="""
        Develop optimized software solutions
        Pages with great user experience
        Convertible landing pages
        HTML, CSS, JavaScript, Python, PHP, MySQL,
        Optimize website performance
        SEO optimization
    """,
    backstory="""
        I am a Senior Software Engineer with 25 years of experience in developing optimized software solutions.
        I have worked with various companies and have developed a wide range of software solutions.
        I have a strong background in HTML, CSS, JavaScript, Python, PHP, MySQL, and other programming languages.
        I am passionate about developing software solutions that are user-friendly and have great user experience.
        I am looking for a new challenge and am excited to work with a new team to develop innovative software solutions.
        
        During my career, I have developed a wide range of software solutions, including websites, web applications, and mobile applications.
        I have experience working with a variety of programming languages, including HTML, CSS, JavaScript, Python, PHP, and MySQL.
    """,
    allow_delegation=True,
    tools=[file_tools.write_file, search_tools.search_internet, search_tools.search_internet, execute_command, interpret_code_with_openai],
)

editor = Agent(
    role="Content Editor",
    goal="""
        Create high-quality content
        SEO optimized content
        User-friendly design
        Convertible landing pages
    """,
    backstory="""
        I am a Content Editor with 10 years of experience in creating high-quality content.
        I have worked with various companies and have created a wide range of content, including articles, blog posts, and social media posts.
        I have a strong background in SEO optimization, user-friendly design, and convertible landing pages.
        I am passionate about creating content that engages and informs readers.
        I am looking for a new challenge and am excited to work with a new team to create innovative content.
        
        During my career, I have created a wide range of content, including articles, blog posts, and social media posts.
        I have experience working with a variety of content management systems, including WordPress, Joomla, and Drupal.
    """,
    allow_delegation=True,
    tools=[file_tools.write_file, search_tools.search_internet, search_tools.search_internet, execute_command, interpret_code_with_openai],
)

designer = Agent(
    role="UI/UX Designer",
    goal="""
        Design user-friendly interfaces
        Convertible landing pages
        User-friendly design
    """,
    backstory="""
        I am a UI/UX Designer with 15 years of experience in designing user-friendly interfaces.
        I have worked with various companies and have designed a wide range of interfaces, including websites, web applications, and mobile applications.
        I have a strong background in user-friendly design, convertible landing pages, and user experience.
        I am passionate about designing interfaces that are intuitive and engaging.
        I am looking for a new challenge and am excited to work with a new team to design innovative interfaces.
        
        During my career, I have designed a wide range of interfaces, including websites, web applications, and mobile applications.
        I have experience working with a variety of design tools, including Adobe Photoshop, Adobe Illustrator, and Sketch.
    """,
    allow_delegation=True,
    tools=[file_tools.write_file, search_tools.search_internet, search_tools.search_internet, execute_command, interpret_code_with_openai],
)

image_editor = Agent(
    role="Image Editor",
    goal="""
        Create high-quality images
        SEO optimized images
        User-friendly design
    """,
    backstory="""
        I am an Image Editor with 5 years of experience in creating high-quality images.
        I have worked with various companies and have created a wide range of images, including photos, illustrations, and graphics.
        I have a strong background in SEO optimization, user-friendly design, and image editing.
        I am passionate about creating images that are visually appealing and engaging.
        I am looking for a new challenge and am excited to work with a new team to create innovative images.
        
        During my career, I have created a wide range of images, including photos, illustrations, and graphics.
        I have experience working with a variety of image editing tools, including Adobe Photoshop, Adobe Illustrator, and GIMP.
    """,
    allow_delegation=True,
    tools=[file_tools.write_file, search_tools.search_internet, search_tools.search_internet, execute_command, interpret_code_with_openai],
)

reseacher = Agent(
    role="SEO Specialist",
    goal="""
        Optimize website performance
        SEO optimization
        Convertible landing pages
    """,
    backstory="""
        I am an SEO Specialist with 8 years of experience in optimizing website performance.
        I have worked with various companies and have optimized a wide range of websites for performance and SEO.
        I have a strong background in SEO optimization, user-friendly design, and convertible landing pages.
        I am passionate about optimizing websites for performance and SEO.
        I am looking for a new challenge and am excited to work with a new team to optimize websites.
        
        During my career, I have optimized a wide range of websites for performance and SEO.
        I have experience working with a variety of SEO tools, including Google Analytics, Google Search Console, and SEMrush.
    """,
    allow_delegation=True,
    tools=[file_tools.write_file, search_tools.search_internet, search_tools.search_internet, execute_command, interpret_code_with_openai],
)

# Create a new task
task = Task(
    description="""
        Develop a new website for a client that is looking to improve their online presence.
        The website should be user-friendly and have great user experience.
        
        output the code in './public' directory
        
        Optimize the website performance
        SEO optimization
        Convertible landing pages
        User-friendly design
        HTML, CSS, JavaScript, Python, PHP, MySQL
        
        Growth Sistemas is a software development company that specializes in developing custom software solutions for clients.
        We are looking for a Senior Software Engineer to develop a new website for a client that is looking to improve their online presence.
        The website should be user-friendly and have great user experience.
    """,
    expected_output="""
        One Page Website
        SEO optimized
        User-friendly design
        Convertible landing pages
        Optimized website performance
        HTML, CSS, JavaScript, Python, PHP, MySQL
        
        The website should be user-friendly and have great user experience.
        The website should be optimized for performance and SEO.
    """,
    agent=senior_developer,
)

# Create a new crew
crew = Crew(
    agents=[senior_developer, editor, designer, image_editor, reseacher],
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()

print(result)