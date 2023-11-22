# PyROOT Macros #

You know how other books go on and on about programming fundamentals
and finally work up to building a complete, working program? In this
guide, we will describe how to write a Python macro that makes use of ROOT commands.

If you have a number of lines which you were able to execute at the PyROOT
prompt, they can be put into a Python ROOT macro `macro.py`

``` {.py}
import ROOT
<          ...
    your lines of Python / PyROOT code
           ...             >
```

We shall build-up a small example macro in a file `macro.py`. First, a small set of options can help making your plot nicer:

``` {.py}
import ROOT

ROOT.gROOT.SetStyle("Plain")   # set plain TStyle
ROOT.gStyle.SetOptStat(111111) # draw statistics on plots, 0 for no output
ROOT.gStyle.SetOptFit(1111)    # draw fit results on plot, 0 for no ouput
ROOT.gStyle.SetPalette(57)     # set color map
ROOT.gStyle.SetOptTitle(0)     # suppress title box
```

Next, we create a canvas for graphical output, with size,
subdivisions and format suitable to your needs, see documentation of
class `TCanvas`:

``` {.py}
c1 = ROOT.TCanvas("c1","<Title>",0,0,400,300) # create a canvas, specify position and size in pixels
c1.Divide(2,2) # subdivide the canvas into 2x2 pads
```

We can then draw a few things into each pad and save the output:
``` {.py}
f2 = ROOT.TF1("f2","[0]*sin([1]*x)/x",0.,10.)

c1.cd(1)       # change to pad 1 of canvas c1
f2.SetParameter(0,1)
f2.SetParameter(1,1)
f2.DrawCopy()

c1.cd(2)       # change to pad 2 of canvas c1
f2.SetParameter(0,1./2.)
f2.SetParameter(1,2)
f2.DrawCopy()

c1.cd(3)       # change to pad 3 of canvas c1
f2.SetParameter(0,1./3.)
f2.SetParameter(1,3)
f2.DrawCopy()

c1.cd(4)       # change to pad 4 of canvas c1
f2.SetParameter(0,1/4.)
f2.SetParameter(1,4)
f2.DrawCopy()

c1.SaveAs("test.pdf")
```

The macro is executed by typing

``` {.sh}
 > python macro.py
```

at the system prompt. You realise this will execute the macro and exit
directly to the shell. You can stay on the python interactive prompty by using

``` {.sh}
 > python -i macro.py
```

You can also run the macro from the interactive Python command line, using these versions (or variations thereof):

``` {.py}
 > python
>>> import macro # using import
>>> ...
>>> exec(open("filename.py").read()) # alternative: reading and excuting file contents directly
```

When using `import`, the variables are accessible in the namespace of
the module, e.g. as `macro.c1`. If you want to change the script and
import again in the same session session as module, you would have to
use a facility like importlib:

``` {.py}
>>> import importlib
>>> importlib.reload(macro)
```

## A more complete example ##

Let us now look at a rather complete example of a typical task in data
analysis, a macro that constructs a graph with errors, fits a (linear)
model to it and saves it as an image. To run this macro, simply type in
the shell:

``` {.sh}
 > python macro1.py
```

The code is built around the ROOT class `TGraphErrors`, which was
already introduced previously. Have a look at it in the class reference
guide, where you will also find further examples. The macro shown below
uses additional classes, `TF1` to define a function, `TCanvas` to define
size and properties of the window used for our plot, and `TLegend` to
add a nice legend.

``` {.py .numberLines}
@ROOT_INCLUDE_FILE macros/macro1.py
```

Let's comment it in detail:

-   Line *4-11*: define the input data and create an instance of the
    `TGraphErrors` class. The constructor
    takes the number of points and the pointers to the arrays of
    x values, y values, x errors (in this case none,
    represented by the NULL pointer) and y errors. The last line
    defines in one shot the title of the graph and the titles of the two
    axes, separated by a ";".

-   Line *13-16*: These lines should be rather intuitive. To understand
    better the enumerators for colours (e.g. `ROOT.kBlue`) and styles
    (e.g. `ROOT.kOpenCircle`) see the reference for the `TColor` and
    `TMarker` classes.

-   Line *19*: the canvas object that will host the drawn objects.

-   Line *22*: the method *Draw* draws the object on the
    canvas. The string option "APE" stands for:

    -   *A* imposes the drawing of the Axes.

    -   *P* imposes the drawing of the graph's markers.

    -   *E* imposes the drawing of the graph's error bars.

-   Line *25*: define a mathematical function. There are several ways to
    accomplish this, but in this case the constructor accepts the name
    of the function, the formula, and the function range.

-   Line *28-29*: Format the line. Try to give a look to the line styles at your
    disposal visiting the documentation of the `TLine` class.

-   Line *32*: fits the *f* function to the graph.
    It is interesting to look at the output on
    the screen to see the parameters values and other crucial
    information given my the minimisation algorithm.

-   Line *33*: draws the fitted line on the canvas. The
    "same" option avoids the cancellation of the already drawn objects,
    in our case, the graph. The function *f* will be drawn using the *same* axis
    system defined by the previously drawn graph.

-   Line *35-41*: completes the plot with a legend, represented by a
    `TLegend` instance. The constructor takes as parameters the lower
    left and upper right corners of the legend, expressed as fractions
    (0.0 -- 1.0) of the total size of the canvas[^1],
    and the legend header string.
    You can add to the legend the objects, previously drawn or not
    drawn, through the `addEntry` method. The final line draws the legend.

-   Line *43-46*: defines an arrow with a triangle on the right hand
    side, a thickness of 2 and draws it.

-   Line *60-61*: put a (Latex) text string on the plot,
    the lower left corner is located in the specified coordinate.
    The `#splitline{}{}` construct allows to store multiple lines
    in the same `TLatex` object.

-   Line *63*: save the canvas as image. The format is automatically
    inferred from the file extension (it could have been eps, gif, ...).
    Note: if you just want to save whatever is the curently active canvas,
    you can also use `ROOT.gPad.SaveAs(...)`

[^1]: (0,0) is the lower left, (1,1) is the upper right

Let's give a look to the obtained plot in Figure [3.1](#f31). Beautiful
outcome for such a small bunch of lines, isn't it?

[f31]: figures/graf_with_law.png "f31"
<a name="f31"></a>

![Your first plot with data points, a fit of an analytical function, a
legend and some additional information in the form of graphics
primitives and text. A well formatted plot, clear for the reader is
crucial to communicate the relevance of your results to the
reader.\label{f31}][f31]

## Summary of Visual effects

### Colours and Graph Markers

We have seen that to specify a colour, some identifiers like kWhite,
kRed or kBlue can be specified for markers, lines, arrows etc. (Because these live in the ROOT namespace, use `ROOT.kWhite` etc, same as for all
other ROOT constants). A
complete summary of colours is represented by the ROOT "[colour
wheel](http://root.cern.ch/root/htmldoc/TColor.html#C02)". To know more
about the full story, refer to the online documentation of `TColor`.

ROOT provides several [graphics
markers](http://root.cern.ch/root/htmldoc/TAttMarker.html#M2) types. Select
the most suited symbols for your plot among dots, triangles, crosses or
stars. An alternative set of names for the markers is available.

### Arrows and Lines

The macro above shows how to define an arrow and draw it. The class
representing arrows is `TArrow`, which inherits from `TLine`. The
constructors of lines and arrows always contain the coordinates of the
endpoints. Arrows also foresee parameters to [specify
their](http://root.cern.ch/root/htmldoc/TArrow.html) shapes. Do not
underestimate the role of lines and arrows in your plots. Since each
plot should contain a message, it is convenient to stress it with
additional graphics primitives.

### Text

Also text plays a fundamental role in making the plots self-explanatory.
A possibility to add text in your plot is provided by the `TLatex`
class. The objects of this class are constructed with the coordinates of
the bottom-left corner of the text and a string which contains the text
itself. Most
[Latex mathematical symbols](http://root.cern.ch/root/htmldoc/TLatex.html#L5)
are automatically interpreted, however you need to replace the "\\" by a "\#".

If
["\\" is used as control character](http://root.cern.ch/root/htmldoc/TLatex.html#L14)
, then the
[TMathText interface](http://root.cern.ch/root/htmldoc/TMathText.html)
is invoked. It provides the plain TeX syntax and allow to access character's
set like Russian and Japanese.

