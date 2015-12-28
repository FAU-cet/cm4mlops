Are you an individual researcher or organization performing
many experiments on a regular basis? You may find the Collective 
Knowledge framework (CK) useful if you suffer from one or more 
of the following problems:

* instead of innovating, you spend weeks and months preparing 
ad-hoc experimental workflows, which you either throw away 
when your ideas are not validated or need to maintain
(adapting to ever changing software, hardware, interfaces and
data formats);

* you have trouble sharing whole experimental workflows 
and results with your colleagues since they use different
operating systems, tools, libraries and hardware
(and they do need to use their latest environment rather 
than possibly outdated Docker or VM images);

* you have trouble managing and reusing your own scripts, tools, 
data sets and reproducing your own results from past projects;

* you have trouble retrieving data from your own or someone else's
"black-box" database (particularly if you do not know the schema);

* you spend lots of time updating your reports and papers whenever
you obtain new results;

* you do not have enough realistic workloads, benchmarks and data sets
for your research;

* you face the ever increasing number of experimental choices
to explore in complex design and optimization spaces;

* you accumulate vast amounts of raw experimental data but do not
know what the data is telling you ("big data" problem);

* you want to extract knowledge from raw data in form of models
but never find time to master powerful predictive analytics techniques;

* your organization pays dearly for its computational needs (in particular,
for hardware and energy used in data centers and supercomputers) 
while you suspect they could be met at a fraction of the cost (if, for example,
your deep learning algorithms could run 10 times faster).

All above problems dramatically slowed down our own
computer systems' research during past 15 years (developing
faster, smaller, more power efficient and reliable computer
systems via multi-objective autotuning, machine learning 
and run-time adaptation) and eventually motivated us to 
develop Collective Knowledge Framework (CK) which brings 
an interdisciplinary community together to collaboratively 
solve above problems.

CK is an open-source, light-weight, portable and
customizable Python-based wrapper framework (less than 1Mb
with minimal dependencies and with a tiny OpenME library
to access CK from C,C++,Fortran,Java,PHP) with a command
line front-end and integrated web server to help scientists
and research engineers:

* abstract and unify access to their software, hardware and data 
via CK modules (wrappers) with a simple JSON API 
while protecting users from continuous low-level changes
and exposing only minimal information needed for research
and experimentation (this, in turn, enables simple 
co-existence of multiple tools and libraries such as 
different versions of compilers including LLVM, GCC and ICC);

* provide a simple and user-friendly directory structure 
(CK repositories) to gradually convert all local artifacts 
(scripts, benchmarks, data sets, tools, results, predictive models, 
graphs, articles) into searchable, reusable and interconnected 
CK entries (components) with unique IDs and open JSON-based meta 
information while getting rid of all hardwired paths;

* quickly prototype research ideas from shared components
as LEGO(TM), unify exchange of results in schema-free JSON
format and focus on knowledge discovery (only when idea
is validated you should spend extra time on adding proper
types, descriptions and tests, and not vice versa);

* easily share CK repositories with whole experimental
setups and templates with the community via popular public
services including GitHub and BitBucket while keeping track
of all development history;

* speed up search across all your local artifacts by JSON
meta information using popular ElasticSearch (optional);

* involve the community or workgroups to share realistic
workloads, benchmarks, data sets, tools, predictive models 
and features in a unified and customizable format;

* reproduce empirical experimental results in a different environment 
and under different conditions, and apply statistical analysis 
(similar to physics) rather than just replicating them 
- useful to analyze and validate varying results
(such as performance and energy);

* use built-in CK web server to view interactive graphs
and articles while easily crowdsourcing experiments 
using spare computational resources (mobile devices, data centers,
supercomputers) and reporting back unexpected behavior; 

* obtain help from an interdisciplinary community to explain 
unexpected behavior when reproducing experiments, solve it 
by improving related CK modules and entries, and immediately 
push changes back to the community (similar to Wikipedia);

* simplify the use of statistical analysis and predictive
analytics techniques for non-specialists via CK modules
and help you process large amount of experimental results
(possibly on the fly via active learning), share and
improve predictive models and features (knowledge), and
effectively compact "big data".

For example, CK already helped our colleagues unify some
of the past computer systems' research, and enable
extensible and multi-objective SW/HW autotuning as a CK
template (workflow). The community now gradually exposes
various tuning choices (algorithm and OpenCL/CUDA/MPI
parameters, compiler flags, polyhedral transformations,
CPU/GPU frequency, etc) and objectives (execution time,
code size, compilation time, energy, processors size,
accuracy, reliability) while reusing shared autotuning and
machine learning plugins to explore optimization spaces.
Our colleagues already managed to speed up some popular
applications with real workloads across latest platforms
(from mobile phones to cloud servers) by 10x with the same
numerical accuracy, reduce energy by 30% and code size
by 50%. Furthermore, such CK templates can be easily reused
in other research scenarios while allowing students and
researchers start new experiments or reproduce others' results
in minutes rather than days and weeks, as described here:
* http://cknowledge.org/repo
* http://github.com/ctuning/ck/wiki/Getting_started_guide_example_slambench
* https://github.com/ctuning/ck/wiki/Getting_started_guide_clsmith

Our long-term mission is to help the research community
dramatically accelerate knowledge discovery via open,
agile, collaborative and reproducible research,
experimentation and knowledge sharing while keeping it as
simple as GitHub and Wikipedia - join us!

For more details, please see our recent vision paper at DATE'16, 
ADAPT workshop, artifact sharing and evaluation initiative for 
computer systems' conferences, and live demo with the CK-based
reproducible and interactive articles:
* http://bit.ly/ck-date16
* http://cTuning.org/ae
* http://adapt-workshop.org
* http://cknowledge.org/repo

Documentation 
=============
* Full CK documentation (including motivation, getting started guide and tutorials): http://github.com/ctuning/ck/wiki
* All shared modules: https://github.com/ctuning/ck/wiki/Shared_modules
* All shared repositories: https://github.com/ctuning/ck/wiki/Shared_repos

License
=======
* Permissive 3-clause BSD license (see LICENSE.txt file for more details).

Authors
=======
* Grigori Fursin, http://fursin.net
* Anton Lokhmotov, https://www.hipeac.net/~anton

Copyright
=========
(C)opyright 2014-2015 Grigori Fursin, Anton Lokhmotov and contributors

Minimal requirements
====================
* Python >= 2.6 (3.0+ is natively supported)
* GIT command line client

If you would like to use shared repositories with already implemented
crowd-benchmarking, multi-objective autotuning, statistical analysis,
predictive analytics, interactive graphs, etc, you may need to install
extra Python packages: 

* 'matplotlib','scipy' and 'numpy' to plot graphs and perform statistical 
analysis (during performance/energy/accuracy autotuning and modeling)
* 'sklearn-kit' for predictive analytics
* 'psutil' to properly terminate running process on Windows after timeout 
(during program autotuning and design space exploration)
* 'Tkinter' or 'tkinter' or 'pyperclip' if copy to clipboard functionality 
is required (to reproduce CK experiments from the web)

Alternatively, you can use Anaconda python distribution
which includes all scientific packages required for CK-based
collaborative and reproducible experimentation.

You can also considerably speed up local search by installing 
free third-party Hadoop-based ElasticSearch (http://elastic.co) 
and turning on transparent indexing in CK.

We successfully validated CK on Linux, Windows, Mac OS X 
and partially on Android.

Minimal installation
====================

Download latest CK from GitHub:

 $ git clone https://github.com/ctuning/ck.git ck

Add ck/bin directory to PATH variable

 $ export PATH=$PWD/ck/bin:$PATH

On Windows, you should manually add full path to ck/bin 
to you PATH environment variable.

If you would like to use CK from ipython notebook or other
python applications, you can install it as a standard 
Python library (you may need root privileges depending 
on how your Python is installed):

 $ cd ck

 $ sudo python setup.py install

By default, CK uses the latest version of installed Python, i.e.
v3 and then v2. You can force CK to use a given Python version
by changing environment variable "CK_PYTHON", i.e.:

 $ export CK_PYTHON=python3
 
 or

 $ export CK_PYTHON=python

Other installation possibilities (via PIP, Conda, Debian) are described
here: https://github.com/ctuning/ck/wiki/Installation 

Basic usage
===========

You can check that CK is installed correctly via:

 $ ck

You should see information about CK options.

If you have IPython installed, you can then check CK library 
installation as following:

 $ ipython

 $ import ck.kernel as ck

 $ ck.test()

 $ ck.access('list module')

 $ ck.access('load kernel default')

Now, you can use CK to pull various shared CK repositories
(code and data shared as reusable components via GitHub
or Bitbucket) and run shared experimental workflows.

For example, we use CK to systematize and accelerate our computer systems' 
research, perform systematic benchmarking across any existing hardware, 
crowdsource multi-objective program optimization, share realistic workloads, 
build predictive models of performance, analyze representative benchmarks 
and data sets, install missing tools, etc. Rather than wasting weeks and
months developing your own ad-hoc experimental setups, you can now obtain,
compile and run any shared benchmark on your Linux machine with GCC 
in less than a minute via:

 $ ck pull repo:ctuning-programs

 $ ck compile program:cbench-automotive-susan --speed

 $ ck run program:cbench-automotive-susan

You will be asked a few questions and for now you can just press Enter 
to select the default choices.

Please refer to CK documentation (https://github.com/ctuning/ck/wiki)
to find out how to compile and run such benchmarks on Windows or Android,
autotune or crowdtune them (performance, energy, accuracy, size, etc),
share other realistic workloads, benchmarks and data sets, apply machine 
learning to explain unexpected behavior or predict optimizations, 
and quickly prototype your own research ideas.

CK also helps you get rid of hardwired paths for your local data sets,
tools and scripts - instead you can simply query CK and obtain all 
shared data sets by specific tags simply via

 $ ck search dataset --tags=image,jpeg

 $ ck find dataset:[name from above list]

You can also easily add your own CK modules to serve
as wrappers (containers) with unified API for your data and
tools while gradually substituting all your ad-hoc scripts.
For example, you can add your own module 'hello' with
an action 'say' and with an entry 'world' as following (you
can select all default values by just pressing Enter):

 $ ck add module:hello

 $ ck add_action module --func=say

 $ ck add hello:world

 $ ck say hello:world

You can now find and customize Python dummy function 'say' 
in the CK module 'hello' (module.py) via
 
 $ ck find module:hello

You can also find associated CK entry hello:say and modify 
its meta information (.cm/meta.json) via

 $ ck find hello:world

Finally, you can start CK web server either to be able
to collect experimental results from other users or to
browse your local artifacts (including interactive graphs
and articles) in a user-friendly way:

 $ ck start web

 $ open browser with URL http://localhost:3344

Please, follow CK documentation (including various Getting Started Guides) for more details:

* https://github.com/ctuning/ck/wiki

Questions/comments/discussions?
===============================
Please, use our mailing lists:
* Open, collaborative and reproducible R&D including knowledge preservation, sharing and reuse:
  http://groups.google.com/group/collective-knowledge
* Software and hardware multi-objective (performance/energy/accuracy/size/reliability/cost)
  benchmarking, autotuning, crowdtuning and run-time adaptation: http://groups.google.com/group/ctuning-discussions

Publications
============
Concepts has been described in the following publications:

* http://bit.ly/ck-date16 (DATE'16)
* http://arxiv.org/abs/1506.06256 (CPC'15)
* http://hal.inria.fr/hal-01054763 (Journal of Scientific Programming'14)
* http://arxiv.org/abs/1406.4020 (TRUST'14 @ PLDI'14)
* https://hal.inria.fr/inria-00436029 (GCC Summit'09)

If you found CK useful and/or interesting, you are welcome
to reference any of the above publications in your articles
and reports.

CK-powered projects
===================

We currently use and improve CK is the following computer systems'
research projects:

* building public repository of realistic workloads, benchmarks, 
data sets, tools, predictive models and optimization knowledge 
in a unified format with the help of the computer engineering 
community (http://github.com/ctuning/ctuning-programs , 
http://github.com/ctuning/reproduce-pamela-project ,
http://github.com/ctuning/reproduce-carp-project ,
http://github.com/ctuning/ctuning-datasets-min ,
http://cknowledge.org/repo , http://c-mind.org/repo)

* implementing universal multi-dimensional,
multi-objective, plugin-based autotuning combined with
crowdsourcing, predictive analytics and run-time adaptation
(to enable self-optimizing computer systems). We support
OpenCL, CUDA, OpenMP, MPI, compiler and any other tuning
for performance, energy, accuracy, size, reliability, cost
and any other metrics across small kernels/codelets and
large applications (http://github.com/ctuning/ck-autotuning, 
http://github.com/ctuning/ck-analytics , 
http://github.com/ctuning/ck-env ,
http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:cd11e3a188574d80).

* implementing crowd-benchmarking (crowdsourcing workload characterization
and compiler heuristic construction across numerous architectures using shared
computational resources such as mobile phones, tablets, cloud services, etc.
(https://play.google.com/store/apps/details?id=com.collective_mind.node ,
http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:cd11e3a188574d80)

* supporting artifact evaluation initiatives for major conferences
and journals where all artifacts are shared as reusable components (and not
just as black box virtual machine images) along with publications
(http://cTuning.org/ae , http://www.dagstuhl.de/de/programm/kalender/semhp/?semnr=15452 ,
http://arxiv.org/abs/1406.4020 , http://adapt-workshop.org)

* enabling open, collaborative and reproducible research and experimentation
with interactive publications focusing on computer engineering
( http://cTuning.org/reproducibility-wiki )

* enabling interactive and reproducible articles for Digital Libraries
(http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:cd11e3a188574d80 ,
http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:6f40bc99c4f7df58)

* serving as a personal knowledge manager to organize, interconnect
and preserve all personal coda and data via simple JSON
meta with UIDs and semantic tags.

You are welcome to add your own CK-powered project here!

Acknowledgments
===============

CK development is coordinated by the non-profit cTuning foundation
(cTuning.org). We would like to thank the EU TETRACOM 609491 project
(www.tetracom.eu) for initial funding and dividiti (www.dividiti.com)
for continuing support. We are also extremely grateful to all volunteers
for their valuable feedback and contributions.
