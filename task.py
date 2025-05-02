from crewai import Task 
from tools import tool 
from agents import news_researcher,news_writer

research_task = Task(
    description = ("Identify your next big trend {topic}"),
    expected_output="A comprehensive 3 paragraph long report on latest ai trends", 
    tools=[tool], 
    agent=news_researcher
    
) 

write_task = Task(
    description = ("compose an insightful article on{topic}"),
    expected_output="A comprehensive 4 paragraph article on latest ai trends", 
    tools=[tool], 
    agent=news_writer, 
    async_execution=False, 
    output_file="new-blog-post.md"
    
) 
