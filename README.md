# ThemeBrand
Updates matplotlib.pyplot.rcParams to suit my style of plotting.

Should be able to drop the ThemeBrand folder directly into your site-packages folder. The location of this folder depends on your installation of python and how you are running it. To find this location, you should be able to run the command [^1] 

> python -c "import site; print(site.getsitepackages()[0])"

in your terminal, and the output should show the path. Placing the ThemeBrand folder directly into this folder should allow importing as usual:

> from ThemeBrand.ThemeBrand import themebrand

Should then be able to use as usual.

In the main folder, 'example-theme-brand.py' demonstrates the usage of the ThemeBrand class.


[^1]: see [this stackoverflow qestion](https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory) for other tips for finding the location.
