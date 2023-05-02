# When to Use Concurrency:

Here's a review some of the key ideas and some decision points that will help determine which, if any, concurrency module I want to use in my project.

The first step of this process is deciding if I should use a concurrency module. While the examples here make each of the libraries look pretty simple, concurrency always comes with extra complexity and can often result in bugs that are difficult to find.

Hold out on adding concurrency until I have a known performance issue and then determine which type of concurrency I need. it is often said, “Premature optimization is the root of all evil (or at least most of it) in programming.”

Once I’ve decided that I should optimize my program, figuring out if my program is CPU-bound or I/O-bound is a great next step. Remember that I/O-bound programs are those that spend most of their time waiting for something to happen while CPU-bound programs spend their time processing data or crunching numbers as fast as they can.

As I saw, CPU-bound problems only really gain from using multiprocessing. threading and asyncio did not help this type of problem at all.

For I/O-bound problems, there’s a general rule of thumb in the Python community: “Use asyncio when I can, threading when I must.” asyncio can provide the best speed up for this type of program, but sometimes I will require critical libraries that have not been ported to take advantage of asyncio. Remember that any task that doesn’t give up control to the event loop will block all of the other tasks.

### Conclusion
I’ve now seen the basic types of concurrency available in Python:

- threading

- asyncio

- multiprocessing

I’ve got the understanding to decide which concurrency method I should use for a given problem, or if I should use any at all! In addition, I’ve achieved a better understanding of some of the problems that can arise when I’m using concurrency.