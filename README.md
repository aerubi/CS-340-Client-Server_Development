# CS-340 Project Two Reflection  
**Grazioso Salvare Rescue Dog Dashboard**  
**Author:** Aero Berry  

---

## How do you write programs that are maintainable, readable, and adaptable?

I write maintainable and readable programs by organizing my code into clearly defined components, using descriptive variable and function names, and adding comments where logic may not be immediately obvious. In this project, the most important example of this approach was the CRUD Python module developed in Project One. By separating all database operations into a single module, I was able to reuse the same code in Project Two without rewriting or duplicating database logic. 

This modular design made the dashboard easier to build and debug because the database access layer was already tested and reliable. If changes are needed in the future, such as modifying queries or connecting to a different collection, those changes can be made in one place without impacting the dashboard code. This approach also improves adaptability, as the same CRUD module could be reused in other projects, such as a different dashboard, a command-line tool, or an API that accesses the same MongoDB database.

---

## How do you approach a problem as a computer scientist?

When approaching this project, I focused first on understanding the client’s requirements and translating them into technical components. For the Grazioso Salvare dashboard, this meant identifying how rescue types mapped to specific database queries and how users would interact with the data through the interface. I broke the problem into smaller parts: database design, query logic, dashboard layout, and interactive behavior.

This approach differed from previous assignments because it required thinking beyond writing isolated code and instead designing a complete system that connects multiple layers. I had to consider usability, data flow, and how changes in one component would affect others. In the future, I would use the same strategy of requirement analysis, modular design, and incremental testing when creating databases for other clients to ensure the final solution meets both technical and user needs.

---

## What do computer scientists do, and why does it matter?

Computer scientists design and build systems that transform raw data into useful information that supports decision-making. In this project, the dashboard helps Grazioso Salvare quickly identify dogs that are good candidates for specific rescue training programs. Without a tool like this, staff would have to manually review large amounts of data, which would be time-consuming and error-prone.

By creating an interactive and data-driven application, this project demonstrates how software can directly support real-world operations. A system like this allows organizations to work more efficiently, make better-informed decisions, and focus their efforts where they matter most. This highlights why computer science is important: it enables organizations to solve complex problems, improve processes, and ultimately make a positive impact through technology.

---
