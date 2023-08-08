
import matplotlib.pyplot as plt

###############################################################################

class themebrand():
    '''
    Theme i wrote so i wouldn't have to keep adding in my lines of updates to the
     matplotlib rcParams.
    If any more themes are wanted, simple define a new theme, the format is the same
     as the other two already here, set_dark_theme and set_latex_theme.
    Alternatively, just edit those current two, to suit your needs.
    '''


    def __init__(self):
        '''
        When initializing the class, this resets the rcParams to their default values.
        Useful when running different scripts with different themes in the same kernel.
        '''
        self.restore_defaults()
        return



    def define_colors(self):
        '''
        If any more colors are desired, add their hex codes to the dictionary below.
        Yes i do realize i don't need to define black, since it is already a defined
         color.
        '''
        self.colors = dict({
            'black'         :'#000000',
            'offwhite'      :'#FFFFDA'
            })
        return



    def set_dark_theme(self):
        '''
        Sets the theme to dark; Black backround, and off-white text and axes, etc.
        Typically the default matplotlib colors 'C0', 'C1', and 'C2' work well on dark
         theme due to their brightness.
        '''
        self.define_colors()
        backcolor = self.colors['black']
        topcolor = self.colors['offwhite']
        plt.rcParams.update({"figure.facecolor" :backcolor,
                             "figure.edgecolor" :backcolor,
                             "axes.facecolor"   :backcolor,
                             "axes.edgecolor"   :backcolor,
                             "savefig.edgecolor":backcolor,
                             "savefig.facecolor":backcolor,
                             "xtick.color"      :topcolor,
                             "ytick.color"      :topcolor,
                             "xtick.minor.visible":True,
                             "ytick.minor.visible":True,
                             "text.color"       :topcolor,
                             "axes.labelcolor"  :topcolor,
                             "axes.edgecolor"   :topcolor,
                             "font.size"        :18,
                             "font.family"      :"serif"
                             })
        return



    def set_latex_theme(self):
        '''
        This is a light theme, with serif font. I was going to make it update some
         other text parameters to make it use LaTeX default fonts and font sizes,
         however python doesn't read my installation of LaTeX so i haven't got around
         to finishing it. It does stll function as a light theme with formal text (font).
        '''
        plt.rcParams.update({"xtick.minor.visible":True,
                             "ytick.minor.visible":True,
                             "font.size"        :18,
                             "font.family"      :"serif"
                             })
        return



    def restore_defaults(self):
        '''
        Resores the default matplotlib parameters.
        '''
        plt.rcdefaults()
        return









