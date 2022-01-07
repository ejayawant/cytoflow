# -*- coding: utf-8 -*-

# (c) Massachusetts Institute of Technology 2015-2018
# (c) Brian Teague 2018-2021
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# CytoFlow documentation build configuration file, created by
# sphinx-quickstart on Fri Mar  6 19:42:50 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, pathlib

# are we running on RTD?
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# select the 'null' pyface toolkit. an exception is raised if the qt toolkit
# is subsequently imported, but that's better than trying to actually create
# a Qt app if PyQt is accidentally imported.

from traits.etsconfig.api import ETSConfig
ETSConfig.toolkit = 'null'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinxext.plot_directive',
]

# Generate the API documentation when building
autosummary_generate = True

# autodoc options
autodoc_member_order = 'bysource'
#autodoc_mock_imports = ['pyface.qt', 'pyface.ui.qt4', 'traitsui.qt4']
autodoc_mock_imports = ['traitsui.qt4']


if on_rtd:
    autodoc_mock_imports.append('cytoflow.utility.logicle_ext.Logicle')
    
# napoleon options
napoleon_use_param = False

# Include the example source for plots in API docs
plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False
plot_working_directory = pathlib.Path(__file__).parents[1].joinpath('cytoflow', 'tests', 'data').as_posix()

plot_pre_code = "import matplotlib.pyplot as plt; plt.switch_backend('agg')"
# plot_rcparams = {'backend' : "Agg"}
# plot_apply_rcparams = True
# plot_pre_code = 'import matplotlib; matplotlib.use("Agg")'

# intersphinx config
intersphinx_mapping = {'pandas' : ('https://pandas.pydata.org/pandas-docs/stable/', None),
                       'envisage' : ('https://docs.enthought.com/envisage/', None),
                       'traits' : ('https://docs.enthought.com/traits/', None),
                       'traitsui' : ('https://docs.enthought.com/traitsui/', None),
                       'pyface' : ('https://docs.enthought.com/pyface/', None),
                       'envisage' : ('https://docs.enthought.com/envisage/', None),
                       'seaborn' : ('https://seaborn.pydata.org/', None),
                       'python': ('https://docs.python.org/3', None),
                       'matplotlib' : ('https://matplotlib.org/', None),
                       'numpy' : ('https://numpy.org/doc/stable/', None),
                       'scipy' : ('https://docs.scipy.org/doc/scipy/reference/', None),
                       'camel' : ('https://camel.readthedocs.io/en/latest/', None)} 


# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Cytoflow'
import time
copyright = u'Massachusetts Institute of Technology 2015-2018, Brian Teague 2018-{}'.format(time.strftime("%Y"))

# Configure the sidebar

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# this is a workaround so we can use versioneer without importing the entire cytoflow module
import versioneer

old_cwd = os.getcwd()
os.chdir(os.path.split(old_cwd)[0])

# The short X.Y version.
version = versioneer.get_version()
# The full version, including alpha/beta/rc tags.
release = versioneer.get_version()

os.chdir(old_cwd)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '*.logicle_ext*.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'any'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'show_powered_by' : False}

html_sidebars = { '**': ['about.html', 'globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'cytoflow'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'Cytoflow.tex', u'Cytoflow Documentation',
   u'Brian Teague', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'cytoflow', u'Cytoflow Documentation',
     [u'Brian Teague'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Cytoflow', u'Cytoflow Documentation',
   u'Brian Teague', 'Cytoflow', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

from typing import List, Tuple, Any, cast
from docutils import nodes
from docutils.nodes import Element, Node
from sphinx import addnodes
from sphinx.errors import NoUri
from sphinx.addnodes import pending_xref

from sphinx.util import logging
from sphinx.transforms.post_transforms import ReferencesResolver

import importlib

logger = logging.getLogger(__name__)

any_preferred = ['cytoflow.operations.i_operation',
                 'cytoflow.views.i_view']

class AnyResolver(ReferencesResolver):
    default_priority = 5

    def run(self, **kwargs: Any) -> None:
        for node in self.document.traverse(addnodes.pending_xref):
            content = self.find_pending_xref_condition(node, ("resolved", "*"))
            if content:
                contnode = cast(Element, content[0].deepcopy())
            else:
                contnode = cast(Element, node[0].deepcopy())

            newnode = None

            typ = node['reftype']
            refdoc = node.get('refdoc', self.env.docname)
            
            try:
                if typ == 'any':
                    newnode = self.resolve_anyref(refdoc, node, contnode)
            except NoUri:
                newnode = None
           
            if newnode:
                newnodes: List[Node] = [newnode]
                node.replace_self(newnodes)
            
    def resolve_anyref(self, refdoc: str, node: pending_xref, contnode: Element) -> Element:
        """Resolve reference generated by the "any" role."""
        stddomain = self.env.get_domain('std')
        target = node['reftarget']
        results: List[Tuple[str, Element]] = []

        # next, do the standard domain (makes this a priority)
        results.extend(stddomain.resolve_any_xref(self.env, refdoc, self.app.builder,
                                                  target, node, contnode))
        for domain in self.env.domains.values():
            if domain.name == 'std':
                continue  # we did this one already
            try:
                results.extend(domain.resolve_any_xref(self.env, refdoc, self.app.builder,
                                                       target, node, contnode))
            except NotImplementedError:
                # the domain doesn't yet support the new interface
                # we have to manually collect possible references (SLOW)
                for role in domain.roles:
                    res = domain.resolve_xref(self.env, refdoc, self.app.builder,
                                              role, target, node, contnode)
                    if res and len(res) > 0 and isinstance(res[0], nodes.Element):
                        results.append(('%s:%s' % (domain.name, role), res))
                        
        # now, see how many matches we got...
        if not results:
            return None
        elif len(results) == 1:
            res_role, newnode = results[0]
        else:
            res_role = None
            
            # first, are we looking for a module?  do we already know about it?
            if 'py:module' in node and node['reftarget'] == node['py:module'].split('.')[-1]:
                for r, n in results:
                    if node['py:module'] == n['reftitle']:
                        res_role, newnode = r, n
                        break

            # second, see if the reference is to any object in the
            # class hierarchy
            if not res_role and 'py:module' in node and 'py:class' in node:
                node_mod = importlib.import_module(node['py:module'])
                node_klass = getattr(node_mod, node['py:class'])
                node_mro = node_klass.mro()
                
                for r, n in results:
                    if r == 'py:attr' or r == 'py:meth':
                        # n_attr = n['reftitle'].split('.')[-1]
                        n_klass = '.'.join(n['reftitle'].split('.')[:-1])
                        if n_klass in [x.__module__ + '.' + x.__qualname__ for x in node_mro]:
                            res_role, newnode = r, n
                            break
                    elif r == 'py:class':
                        # in same module?
                        n_mod = '.'.join(n['reftitle'].split('.')[:-1])
                        if 'py:module' in node and node['py:module'] == n_mod:
                            res_role, newnode = r, n
                            break
                    else:
                        logger.warning("Could not handle role {}".format(r),
                                       location = node)
            
            # check if any result starts with a prefix in any_preferred
            if not res_role:
                for r, n in results:
                    for p in any_preferred:
                        if n['reftitle'].startswith(p):
                            res_role, newnode = r, n
                            break
                     
                    if res_role:
                        break
# 
#             # check to see if any result is shorter (ie, a base class)
#             if not res_role:
#                 def num_elements(result):
#                     r, n = result
#                     return len(n['reftitle'].split('.'))
#                 
#                 res_sorted = sorted(results, key = num_elements)
#                 if num_elements(res_sorted[0]) < num_elements(res_sorted[1]):
#                     res_role, newnode = res_sorted[0]
                    
            if not res_role:         
                def stringify(name: str, node: Element) -> str:
                    reftitle = node.get('reftitle', node.astext())
                    return ':%s:`%s`' % (name, reftitle)
                candidates = ' or '.join(stringify(name, role) for name, role in results)
                logger.warning('more than one target found for \'any\' cross-'
                                  'reference %r: could be %s', target, candidates,
                               location=node)
            
                res_role, newnode = results[0]

        # Override "any" class with the actual role type to get the styling
        # approximately correct.
        res_domain = res_role.split(':')[0]
        if (len(newnode) > 0 and
                isinstance(newnode[0], nodes.Element) and
                newnode[0].get('classes')):
            newnode[0]['classes'].append(res_domain)
            newnode[0]['classes'].append(res_role.replace(':', '-'))
        return newnode
        

def setup(app):    
    app.add_post_transform(AnyResolver)

    app.connect('builder-inited', convert_notebooks)
    app.connect('builder-inited', run_apidoc)
    app.connect('autodoc-process-docstring', process_docstring)
    sys.modules['sys'].IN_SPHINX = True
    
def convert_notebooks(app):
    from nbconvert.nbconvertapp import NbConvertApp
    from traitlets.config import Config
    from shutil import copy2
    
    curr_dir = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
    
    notebooks_basic = (curr_dir / 'examples-basic').glob('*.ipynb')
    dest_dir = curr_dir / 'dev_manual' / 'tutorials'
    images_dir = dest_dir / '_images'
    images_dir.mkdir(exist_ok = True)

    for notebook_file in notebooks_basic:
        output_name = notebook_file.stem.lower()
        output_name = output_name.replace(' ', '_')
        
        c = Config()
        c.NbConvertApp.export_format = 'rst'
        c.NbConvertApp.output_base = output_name
        c.FilesWriter.build_directory = str(dest_dir)
        c.NbConvertApp.notebooks = [str(notebook_file)]
        
        app = NbConvertApp(config = c)
        app.init_writer()
        app.convert_notebooks()
        
        images = notebook_file.parent.glob('_images/*')
        
        for image_file in images:
            copy2(image_file, images_dir)


    notebooks_advanced = (curr_dir / 'examples-advanced').glob('*/*.ipynb')
    dest_dir = curr_dir / 'dev_manual' / 'examples'
    images_dir = dest_dir / '_images'
    images_dir.mkdir(exist_ok = True)
    
    for notebook_file in notebooks_advanced:
        output_name = notebook_file.stem.lower()
        output_name = output_name.replace(' ', '_')
        
        c = Config()
        c.NbConvertApp.export_format = 'rst'
        c.NbConvertApp.output_base = output_name
        c.FilesWriter.build_directory = str(dest_dir)
        c.NbConvertApp.notebooks = [str(notebook_file)]
        
        app = NbConvertApp(config = c)
        app.init_writer()
        app.convert_notebooks()
        
        images = notebook_file.parent.glob('_images/*')
        
        for image_file in images:
            copy2(image_file, images_dir)
    
    
def run_apidoc(app):
    
    # os.environ['SPHINX_APIDOC_OPTIONS'] = 'no-undoc-members'

    from sphinx.ext.apidoc import main
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    curr_dir = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
    
    output_dir = curr_dir / "dev_manual" / "api"
    
    module = curr_dir / ".." / "cytoflow"    
    main(['-T', '-e', '-f', '-M', '-E', '-o', str(output_dir), str(module), str(module / "tests" / "*"), str(module / "utility" / "logicle_ext")])
    

    module = curr_dir / ".." / "cytoflowgui"
    main(['-T', '-e', '-f', '-M', '-E', '-o', str(output_dir), str(module), str(module / "tests" / "*")])
#     
#     module = curr_dir / ".." / "fcsparser"
#     main(['-T', '-e', '-f', '-M', '-E', '-o', str(output_dir), str(module), str(module / "tests" / "*")])


def process_docstring(app, what, name, obj, options, lines):
    if what == 'module' and len(lines) > 2 and not options.noindex:
        name = obj.__name__
        lines[0] = name
        lines[1] = '-' * len(name)
