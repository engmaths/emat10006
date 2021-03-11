# Assignment


## Overview

This is a group project to be completed in groups of ~5 students. You should
work together on a single codebase but each of you should contribute some
individual parts of the code.

You will produce a joint submission as a group in a single GitHub repo and an
individual report to be submitted to Blackboard:

* Code (on GitHub)
* Project Report (on GitHub)
* Reflection Report (submitted individually on Blackboard)

The project is open-ended with the exact goal to be decided amongst your group
but the theme is around simulations and data relating to the coronavirus
epidemic. You should make a program or several programs that can either run
simulations or produce plots based on real data.

You should collaborate and share your code using a **private** repository on
GitHub. The repository should be shared with your TA: the code that is present
on GitHub at the time of the deadline will be treated as being your
submission for this project.

Along with your code there should be a group Project Report explaining your
code and what it does and including some figures that are output from your
code or perhaps links to videos or any other output.

Each of you should write a short individual Reflection Report which explains
your own contributions to the project and reflects on how you and the rest of
the team worked collaborated together. This is to be submitted through
Blackboard.

**Note**: While this is mainly about code contributions indivdual marks will
be based on the Reflection Report in Blackboard. If you do not submit the
Reflection Report you will get a mark of zero for the whole project. If you
submit it late then lateness penalties will apply to the mark for the whole
project.


## Example

An example of a program that runs some simulations can be found
[here](simulator.py). For examples of usage look inside the code which has
explanations in the docstrings and comments. This was also discussed in the
live session (see the recording on Blackboard).

If you run the script you should see something like this:

~~~
<iframe width="560" height="315"
src="https://www.youtube.com/embed/gBtmIR50w7Q" frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;
picture-in-picture" allowfullscreen>
</iframe>
~~~

Some key points to note about this example code:

* It is possible to run simulations with different parameters by running with
  different command line arguments or by calling the functions with different
  arguments (it is not necessary to edit the code to run with different
  parameters).
* The same simulation code can be used to produce different kinds of outputs
  e.g. on screen animation, plot in a file.
* The same animation and plotting code could also be used with different kinds
  of simulation (e.g. if an alternative version of the Simulation class was
  made).
* The interface and relationships between the classes has been *designed*
  (e.g. which methods should be called by which other classes).
* Docstrings give examples of how to use the different functions and classes
  along with explanations of details that are important in understanding what
  the code does.
* Comments are used to clarify the other overall structure of the code, or to
  explain things that are *not obvious* from the code itself but that will
  help someone looking at that particular bit of code.


## Code

The example code linked above is intended to illustrate several points but
actually you should submit a repository with multiple files in it. For example
here the animation classes could be moved into a file called `animation.py`.
The `Simulation` class could be moved into a file called `simulation.py`. Then
the `main` function could go into a file called `runsim.py`.

At that point you would have a more scalable organisation of code: more types
of simulation could be added in `simulation.py`. More ways to animate could be
added in `animation.py`. There could be more top-level scripts like
`runsim_model2.py` to run different kinds of animation/simulation. These
scripts could do different things and make different plots but reusing the
*same* code from `animation.py` and `simulation.py`.

You should make good use of functions and classes in your project. It is not
strictly necessary to use classes although it might be the best way to
organise some parts of your code. The important point is to have good clean
code:

* No global variables (although global constants are allowed)
* Design a collection of functions/classes that work together in a coherent
  way. Give those functions and classes good clear names.
* Make different parts of your code reusable even if you do not actually use
  them more than once in the project.
* Make your code understandable - someone who has not seen the code before
  should be able to look at the docstrings and the function names and
  understand what they do.
* They should also be able to look at the docstring at the top of each module
  and understand what the whole module is for. The README file should explain
  what the whole repo does.

Before you write any code come up with an overall *design* of the codebase:

* What things will it be possible to do with the code and how?
* What functions or classes will you make in order to achieve this?
* How will those functions or classes be used?
* Can you give those functions and classes a consistent naming scheme that
  emphasises their simularities, differences and relationships?
* What files will you have to organise the code?
* Which parts of the code depend on which other parts?

Your repository should also have a `README.md` file which you can use to
explain from a high-level how to run the programs from the repository after
cloning it. An `md` file can be plain text or it can be formatted using
markdown:
<https://guides.github.com/features/mastering-markdown/>

If you have data in your project then (unless the data files are large) it
should be inluded in the repository in a text-based format such as a `.csv`
file. It is important to note that you should not generally store binary files
such as Microsoft Excel spreadsheets in a GitHub repo as it can only store
textual data efficiently. Also if you commit large files then GitHub will not
allow you to push them.


## Project Report

Your Project Report can be in any format e.g. Word, LaTeX, Markdown, Jupyter
Notebook and should be stored in your GitHub repo. Note though that a binary
Word file can not be efficiently stored in git so if you want to add your
report as a Word document then just add it once at the very end of your
project (when you will not need to make any further changes).

The report should not be long. The purpose of the report is to succinctly
explain any models you are using or data that you have obtained and to show
the resulting plots that you have made. This project is about code (rather
than modelling, data analysis, or epidemiology) so the report should be about
showcasing some outputs of your code and explaining how your code can be used
to produce those as well as other outputs. A minimum of explanation is needed
for those outputs to be understandable but you do **not** need to have a
"background" section or a "literature review" or anything like that - It would
be reasonable to include links to any references though e.g. if your models
are inspired by something else.

You should make your plots look really good with good labels, legends and
captions. Think carefully about the colours you use, the thickness of lines,
the size of text. A lot goes into the design of a good plot:

* What about using subplots to have many plots in one figure?
* Is there a way that you can combine multiple plots to make a single plot
  that conveys the same information more compactly?
* Should your plots be on linear or logarithmic (or semilog) scales?
* Does it make sense to use a line or markers or perhaps a barchart?
* Should your plot have error bars?
* Can you annotate key information on the plot?

Think of this report as being like an essay where almost all of the marks are
for how good your figures (or linked videos etc) are.


# Reflective Report

A template will be provided for the individual reflective report:

(ADD TEMPLATE HERE...)

Each of you should submit an individual reflective report explaining your own
contributions and how you and your team have collaborated. This information
along with your TA's record of contributions and attendance will be used in
giving each student an individual mark for the project.


# Collaboration

You should plan how you and your team are going to collaborate on the same
codebase. There should be a plan for who is going to produce which parts of
the code and how those parts are going to work together e.g.:

* Who is going to write each part of the code?
* Which parts of the code use which other parts?
* How will you try to avoid merge conflicts?
* How will each of you test that your changes are not causing someone else's
  code to stop working? (This should be checked before each `git push`)

If each of you writes separate code and happens to store that code in the same
repo in different files with no relation between them then that is a simple
strategy for avoiding conflicts. However that is not really *collaborating* on
the same code. You should be writing code (e.g. functions and classes) for
others to use and using code that others have written. How well you have
successfully managed to work as a team will be assessed as part of this.

As well as looking at how well you have collaborated we will also look at what
your individual contributions are. Sometimes it is good to work in pairs on a
particular part of the code where one of you writes the code and the other
watches and makes suggestions (this is "pair coding"). That is good practice
and if you do that then you should both record that in your Reflection
Reports. However there must be commits from each member of the team: it is
possible to tell from git who has committed what changes to the code. If there
is no evidence of contributions in the commits then you can not be given
credit for your contributions. If you are going to practice pair coding then
it needs to be done both ways around so that you take in turns to do the
writing and committing.


# Rough markscheme

Marking will first consider a mark for the project as a whole. You will be
asked whether you are happy to share the same mark among all members of the
group and if everyone agrees then you will all get the same mark for the
project. Otherwise each individual student will get a different mark based on
our assessment of individual contribution. For this we will look at our own
records of engagement and contribution in the group meetings, the commits
recorded in git and what everyone has written in their Reflection Reports.

The main things that we want to see are:

* Collaboration
* Readable, documented code
* Designed and reusable code
* Quality outputs (e.g. nice plots, although it doesn't have to be plots)
* A report that explains these things

A basic project would be something like:

* Each member of the group has made a script that does some simulation or uses
  some data.
* Each script makes a reasonable plot (with labels etc).
* The report explains what has been done and shows the plots.
* The code is well organised and neatly written.
* Everyone has made reasonable commits to the repository.
* The README explains (correctly) how to use the code.

A good project would be something like:

* The code is well organised into files with reusable functions and maybe
  classes
* Different simulations or plots etc are using shared reusable code
* Different members of the group are working on the same parts of the code
  and/or reusing the functions/classes that other members have made.
* There is a high-level organisation in the files of the codebase
* There is design in how a collection of functions/classes have been put
  together.
* The code is documented in a consistent and clear way and is understandable
  to someone else navigating the repository for the first time.
* The code can be used to generate many different outputs e.g. by using
  command line arguments.
* The different outputs from the project make sense as part of a coherent
  whole (e.g. to evaluate some hypothesis or answer some general question)
* The report explains how the different parts of the project can be combined
  coherently to draw meaningful conclusions (e.g. comparison of model and
  data)
* The plots or other outputs are carefully designed to look good and convey
  lots of information and have good captions.

There are many things that might make sense for some projects but not others
such as using testing or exceptions, classes, packages etc. It is up to you
whether to include these if it makes sense to include them. Note that there
are no tests in the provided example code because it's hard to test animation
code and the simulations are non-deterministic which is also hard to test.

Over the next few weeks we will mention other things that you may or may not
want to include in your projects. Making use of any features or extras that
make sense for your project is good practice and will be noted when marking
but there are no hard rules about what you must use.


## Ideas

There are lots of different ways of modelling epidemics:

* Agent-based modelling (e.g. simulating interacting people). The simulator
  script I've given does that but with the people on a grid. You can also do
  it with the people moving around and infecting each other or with a more
  complicated connectivity than a grid.

* You can also not model individual people but instead the total number of
  infected people e.g. there are 10000 people and 100 are infected. The next
  day there will be approximately 120 infected people (using random numbers
  somehow).

* You can also use continuous numbers with differential equations (e.g. SIR
  model).

You can find discussion and examples here:
<https://towardsdatascience.com/covid19-top-7-online-interactive-simulations-curated-fa4282889875>

There are many different things that you could consider in a model such as:

* Vaccinated people
* Partial immunity
* Numbers of people in hospital

There's also loads of data for different countries, different regions etc. The
UK government gives daily totals for the whole of the UK for both positive
tests and deaths. Those are also broken down by local authority (e.g. Bristol,
North Somerset etc). You can even get weekly data for areas of Bristol (St
Pauls, Clifton, ...).

I think it would be really interesting to focus on a local epidemic in Bristol
and look at the different areas over time. The outbreak has been very
different in student areas for example: Stoke Bishop and City Centre had
pretty much the highest rates in the country in late October but are now down
to almost zero (have the halls reached herd immunity?). You could also compare
Bristol with say Manchester or some other city or the UK with another country.

There are many places to get this data but UK government data available here
(note that you can download the data in e.g. a spreadsheet).

<https://coronavirus.data.gov.uk/details/interactive-map>

There are lots of places to read about covid data presentation. You can find
some discussion and examples here:

<https://www.computerweekly.com/feature/Covid-19-and-the-art-and-science-of-data-visualisation>

Comparison of simulations with data are also interesting. Perhaps some members
of the group could make simulations and others could collect data and you
could devise some way of comparing them to evaluate different models and/or
make predictions for the future. There are lots of questions that you could
think about using either data or modelling or both like how to ease
restrictions while carrying out a vaccination program, best strategies for
lockdowns and so on.

These ideas are deliberately vague. If you have an idea for something quite
different then I'm happy to discuss whether that would make a reasonable
project - please begin by discussing with your TA.
