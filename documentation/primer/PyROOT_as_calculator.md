# PyROOT Basics #

We assume that you managed to install ROOT including the PyROOT bindings.
The guide will assume Python3 and a recent ROOT version, but probably the
dependence on this is low.

## ROOT as calculator (without Python) ##

ROOT has an interactive shell that is capable to interpret C++ code.
While we will not pursue this deeply at this stage, the following
sequence give a basic idea of this.

Launch the ROOT interactive shell with the command

``` {.cpp}
 > root
```

on your Linux box. The prompt should appear shortly:

``` {.cpp}
root [0]
```

and then you may compute things:

``` {.cpp}
root [0] 1+1
(int) 2
root [1] 2*(4+2)/12.
(double) 1.000000
root [2] sqrt(3.)
(double) 1.732051
root [3] 1 > 2
(bool) false
root [4] TMath::Pi()
(double) 3.141593
root [5] TMath::Erf(.2)
(double) 0.222703
root [6] .q
```

Note the probably unexpected form of the quit command: `.q`

You can see that ROOT offers you the possibility not only to
type in `C++` statements, but also advanced mathematical functions,
which live in the `TMath` namespace.

## PyROOT as calculator ##

Obviously, there is an interactive Python shell, completely
independent of ROOT and we shall start off with the same sequence as
in the previous section. Launch Python with the command

``` {.py}
 > python
```

on your Linux box. The prompt should appear shortly (in a similar form):

``` {.py}
Python 3.9.12 (main, Jun  7 2022, 16:09:12) 
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

and then you may compute things:

``` {.py}
>>> 1+1
2
>>> 2*(4+2)/12.
1.0
>>> import math
>>> math.sqrt(3.)
1.7320508075688772
>>> 1 > 2
False
```

Now let's start to access some ROOT constants and functions from the
`TMath` namespace.

``` {.py}
>>> import ROOT
>>> ROOT.TMath.Pi()
3.141592653589793
>>> ROOT.TMath.Erf(.2)
0.22270258921047845
>>> exit()
```

Leaving the Python shell works with <kbd>CTRL</kbd>+<kbd>D</kbd> (be
careful) or `exit()`. From now on we assume you know how to start the
Python shell, import necessary modules and exit.

Now let's do something more elaborated -- it's actually pure Python,
no dependence on ROOT (yet). A numerical example with the well known
geometric series:

$$
\sum_{i=0}^{N-1} x^i = \frac{1 - x^{N}}{1-x}
$$

``` {.py}
>>> x=.5
>>> N=30
>>> geom_series=0.
>>> for i in range(N):
...     geom_series += x**i
... 
>>> print(geom_series - (1-x**N)/(1-x))
0.0
```

Here we made a step forward. We even declared variables and used a
*for* control structure. Note that as usual in Python code blocks
(e.g. in loops) are given by the indentation. Hitting <Enter> on an
indented line (starting with `...`) will move one block up.

From now on, we shall suppress the prompts `>>>` and `...`. To allow a
straight copy-and-paste, there will always an additional empty line
whenever we jump one block out.

## ROOT as function plotter ##

Using one of ROOT's powerful classes, here `TF1` [^2], will allow us to
display a function of one variable, *x*. Try the following:

``` {.y}
f1 = ROOT.TF1("f1","sin(x)/x",0.,10.)
f1.Draw()
```

`f1` is an instance of the ROOT class `TF1`. The arguments used
in the constructor are:

1. a string is a name to be entered in the internal ROOT memory management system;
2. a second string to define the function, here `sin(x)/x`
3. two floating point numbers to define the range of the variable `x`.

The `Draw()` method, here used without any parameters, displays the
function in a window which should pop up after you typed the above two
lines.

A slightly extended version of this example is the definition of a
function with parameters, called `[0]`, `[1]` and so on in the ROOT
formula syntax. We now need a way to assign values to these parameters;
this is achieved with the method
`SetParameter(<parameter_number>,<parameter_value>)` of class `TF1`.
Here is an example:

``` {.py}
# This is Python
f2 = ROOT.TF1("f2","[0]*sin([1]*x)/x",0.,10.)
f2.SetParameter(0,1)
f2.SetParameter(1,1)
f2.Draw()
```

Initially, this version shows the same results. Try setting the
parameters differently and observe how the function changes.

The class `TF1` has a large number of very useful methods, including
integration and differentiation. To make full use of this and other
ROOT classes, visit the documentation on the Internet under
<https://root.cern/doc/master>. As ROOT is natively C++, you may have
to make a translation. E.g. the C++ equivalent of the above code is
given by the very similar looking

``` {.cpp}
# This is C++
TF1 *f2 = new TF1("f2","[0]*sin([1]*x)/x",0.,10.);
f2->SetParameter(0,1);
f2->SetParameter(1,1);
f2->Draw();
```

Note that C++ namespaces require the use of `::`, while in PyROOT this
generally becomes a simple `.`. Thus, the equivalent of PyROOT
`ROOT.TMath.Pi()` in C++ is `TMath::Pi()`.

## Plotting Measurements ##

To display measurements in ROOT, including errors, there exists a
powerful class `TGraphErrors` with different types of constructors. In
the example here, we use data from the file `ExampleData.txt` in text
format:

``` {.py}
gr = ROOT.TGraphErrors("macros/ExampleData.txt")
gr.Draw("AP")
```

You should see the output shown in Figure [2.2](#f22).

[f22]: figures/TGraphErrors_Example.png "f22"
<a name="f22"></a>

![Visualisation of data points with errors using the class TGraphErrors. \label{f22}][f22]

Make sure the file `ExampleData.txt` is available in the directory indicated: it is a simple
text file with lines of four real numbers each, representing the x- and y- coordinates and their
errors of each data point:
```
# fake data to demonstrate the use of TGraphErrors
# x    y    ex    ey
  1.   0.4  0.1   0.05
  1.3  0.3  0.05  0.1
  1.7  0.5  0.15  0.1
  1.9  0.7  0.05  0.1
  2.3  1.3  0.07  0.1
  2.9  1.5  0.2   0.1
```

The argument of the method `Draw("AP")` is important here. Behind the scenes,
it tells the `TGraphPainter` class to show the axes and to plot markers at the
*x* and *y* positions of the specified data points. Note that this simple
example relies on the default settings of ROOT, concerning the size of
the canvas holding the plot, the marker type and the line colours and
thickness used and so on. Eventually, you may want to
specify options explicitly in order to obtain nice and well
readable results. A full chapter on graphs will explain many
more of the features of the class `TGraphErrors` and its relation to
other ROOT classes in much more detail.

## Histograms in ROOT ##

Frequency distributions in ROOT are handled by a set of classes derived
from the histogram class `TH1`. We use here `TH1D`, where the letter `D`
stands for "double", the data type used to store
the entries in one histogram bin.

The following code fills a histogram with 1000 numbers following an
exponential distribution:
``` {.py}
efunc = ROOT.TF1("efunc","exp([0]+[1]*x)",0.,5.)
efunc.SetParameter(0,1)
efunc.SetParameter(1,-1)
h = ROOT.TH1D("h","example histogram",100,0.,5.)
for i in range(1000):
    h.Fill(efunc.GetRandom())

h.Draw()
```

The first three lines of this example define a function, an exponential
in this case, and set its parameters. In line *3* a histogram is
created, with a name, a title, a certain number of bins (100 of
them, equidistant, equally sized) in the range from 0 to 5.

[f23]: figures/TH1F_Example.png "f23"
<a name="f23"></a>

![Visualisation of a histogram filled with exponentially distributed,
random numbers. \label{f23}][f23]

We use a feature of ROOT to fill this histogram with data randomly
generated following a given function using the method
`TF1::GetRandom`. Data is entered in the histogram at line *4* using
the method `TH1::Fill` in a loop construct. As a result, the
histogram is filled with 1000 random numbers distributed according to
the defined function. The histogram is displayed using the method
`TH1::Draw()`.  You may think of this example as repeated
measurements of the life time of a quantum mechanical state, which are
entered into the histogram, thus giving a visual impression of the
probability density distribution.  The plot is shown in Figure
[2.3](#f23).

Note that you will not obtain an identical plot when executing the lines
above, depending on how the random number generator is initialised.

The class `TH1` does not contain a convenient input format from plain
text files. The following lines show how to read an input text file
"expo.dat" (using Numpy, a Python package you will probably be familiar
already) and fill the numbers one-by-one in the histogram until end of
file is reached.

``` {.py}
import ROOT
import numpy as np
h = ROOT.TH1D("h","example histogram",100,0.,5.)
mydata = np.loadtxt('macros/expo.dat')
for x in mydata:
    h.Fill(x)

h.Draw()
```

Histograms and random numbers are very important tools in statistical
data analysis, a whole chapter will be dedicated to this topic.

## Interactive ROOT ##

Look at one of your plots again and move the mouse across. You will
notice that this is much more than a static picture, as the mouse
pointer changes its shape when touching objects on the plot. When the
mouse is over an object, a right-click opens a pull-down menu displaying
in the top line the name of the ROOT class you are dealing with, e.g.
`TCanvas` for the display window itself, `TFrame` for the frame of the
plot, `TAxis` for the axes, `TPaveText` for the plot name. Depending on
which plot you are investigating, menus for the ROOT classes `TF1`,
`TGraphErrors` or `TH1` will show up when a right-click is performed on
the respective graphical representations. The menu items allow direct
access to the members of the various classes, and you can even modify
them, e.g. change colour and size of the axis ticks or labels, the
function lines, marker types and so on. Try it!

<!--
[f24]: figures/ROOTPanel_SetParameters.png "f24"
<a name="f24"></a>

![Interactive ROOT panel for setting function parameters.\label{f24}][f24]
-->

Have a look back at the function plotted in the beginning with two
parameters (`[0]*sin([1]*x)/x`): right-click on the function line and
select "SetLineAttributes", then left-click on "Set Parameters". This
gives access to a panel allowing you to interactively change the
parameters of the function.
<!--, as shown in Figure [2.4](#f24).-->
When clicking on "Apply", the function plot is updated to
reflect the actual value of the parameters you have set.

[f25]: figures/ROOTPanel_FitPanel.png "f25"
<a name="f25"></a>

![Fit Panel. \label{f25}][f25]

Another very useful interactive tool is the `FitPanel`, available for the
classes `TGraphErrors` and `TH1`. Predefined fit functions can be selected
from a pull-down menu, including "`gaus`", "`expo`" and "`pol0`" - "`pol9`"
for Gaussian and exponential functions or polynomials of degree 0 to 9,
respectively. In addition, user-defined functions using the same syntax as
for functions with parameters are possible.

After setting the initial parameters, a fit of the selected function to the
data of a graph or histogram can be performed and the result displayed on the plot.
The fit panel is shown in Figure [2.5](#f25). The fit panel has a number of control options to
select the fit method, fix or release individual parameters in the fit, to steer
the level of output printed on the console, or to extract and display additional
information like contour lines showing parameter correlations. As function fitting
is of prime importance in any kind of data analysis, this topic will again show up
later.

If you are satisfied with your plot, you probably want to save it. Just
close all selector boxes you opened previously and select the menu item
`Save as...` from the menu line of the window. It will pop up a file
selector box to allow you to choose the format, file name and target
directory to store the image.

Using ROOT's interactive capabilities is useful for a first exploration
of possibilities. Other ROOT classes you will encounter in this tutorial
have such graphical interfaces. We will not comment further on this,
just be aware of the existence of ROOT's interactive features and use
them if you find them convenient. Some trial-and-error is certainly necessary
to find your way through the huge number of menus and parameter
settings.

## ROOT initial configuration

You may find that you want to configure some things for every startup
of a PyROOT session. This can be done using the "global pointers" and
e.g. stored in a Python configuration script that you `import` at the
beginning, further explanation below:

``` {.py}
import ROOT, sys, math

# plotting options
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetLabelSize(.05,"xyz")
ROOT.gStyle.SetTitleSize(.05,"xyz")
ROOT.gStyle.SetPadBottomMargin(.18)
ROOT.gStyle.SetPadLeftMargin(.15)
ROOT.gStyle.SetPadRightMargin(.1)

ROOT.gStyle.SetLabelOffset(.01,"y")
ROOT.gStyle.SetTitleOffset(1.3,"y")
ROOT.gStyle.SetTitleOffset(1.3,"x")

ROOT.gStyle.SetTitleW(1.)
ROOT.gStyle.SetTitleStyle(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetMarkerStyle(20)
```

-   **[gROOT](http://root.cern.ch/root/htmldoc/TROOT.html)**: the `gROOT`
    variable is the entry point to the ROOT system. Technically it is an
    instance of the `TROOT` class. Using the `gROOT` pointer one has
    access to basically every object created in a ROOT based program.
    The `TROOT` object is essentially a container of several lists
    pointing to the main `ROOT` objects.

-   **[gStyle](http://root.cern.ch/root/htmldoc/TStyle.html)**: By default
    ROOT creates a default style that can be accessed via the `gStyle`
    pointer. This class includes functions to set some of the following
    object attributes.

    -   Canvas
    -   Pad
    -   Histogram axis
    -   Lines
    -   Fill areas
    -   Text
    -   Markers
    -   Functions
    -   Histogram Statistics and Titles
    -   etc ...

At this point you have already learnt quite a bit about some basic
features of ROOT.

***Please move on to become an expert!***

[^2]: All ROOT classes' names start with the letter T. A notable exception is
RooFit. In this context all classes' names are of the form Roo*. Starting with
ROOT7, all names start with and R.
