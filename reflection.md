# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design was Owner, DailyPlan, and Tasks. I knew I needed to have a lot of tasks that would initialize the tasks in the systems. Then I talked with my AI and realized I need the Scheduler and Pet to reduce the amount of syntax.

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

Some design changes were the filtering tasks had to be implemented so that it would calculate the time based on when the owner dropped off the pet and was going to pick them up. I also needed to add "add task" to the code because without it, the scheduler wouldn't be able to choose the task. 

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers the amount of time the owner has and the priority of the tasks. I had to think about based on a limited amount of time and what the owner would want. 

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

Some tradeoffs are limiting the scheduler to a greedy first-fit strategy, it picks tasks in order until time runs out, rather than searching for the best possible combination. For example, if a 30-minute task is added first and only 25 minutes remain, a 25-minute task that would fit perfectly gets skipped, even though dropping the 30-minute task would have allowed it

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

I had it debugging the code that didn't work and aid me in writing test to pin point the exact problem with the code. The most helpful prompts I used were onces where I would ask the AI to guide me and not fill it in for me when writing the code. 

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

When the AI helped me write filter_tasks, it suggested sorting tasks by priority into a new variable. I kept that idea but ran the code myself with my four test tasks to check which ones actually ended up in the plan. I realized the sorted variable wasn't being used in the loop, so I had to verify the behavior manually rather than just trusting the output looked right. That moment taught me to trace through the logic step by step instead of assuming the AI's suggestion was complete.

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

I tested that the scheduler correctly added tasks within Maria's available window (0 to 500 minutes), that display_plan printed all scheduled tasks with their priority, and that detect_conflicts correctly reported no warning when all tasks fit. I also checked that explain_task returned the right total task count and minutes. These tests were important because they confirmed the full loop was working — from creating tasks and an owner all the way to producing a readable daily plan and checking for conflicts.

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

I am fairly confident the scheduler works for the normal case where there is enough time for all the tasks. I am less confident about edge cases. If I had more time, I would test what happens when the available window is 0, when two tasks have the same priority, and when a task has a duration of 0 like Walk Again in my test. I would also want to make sure the priority sort actually changes which tasks get included when time is tight, since right now sorted_tasks is created but not used in the loop.

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

I am most satisfied with how the class structure came together. Each class has a clear job — CareTask holds task data, Pet holds the pet, Owner holds the constraints, DailyPlan builds the schedule, and Scheduler handles the decision-making. Once I had that separation clear in my head, writing the individual methods felt a lot more manageable.

- What part of this project are you most satisfied with?

**b. What you would improve**

I would fix filter_tasks so it actually iterates over the sorted list instead of the original unsorted one — right now sorted_tasks gets created but never used in the loop. I would also redesign the logic so that when time is limited, high-priority tasks always make it in before lower-priority ones, even if a lower-priority task came first in the list.

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

The biggest thing I learned is that AI is most useful when you already have a rough idea of what you want. When I described the problem in my own words first and then asked for help, the suggestions made sense and I could evaluate them. Designing systems is really about making decisions and being able to explain why — AI can help you think through options, but you still have to own the reasoning.

- What is one important thing you learned about designing systems or working with AI on this project?
