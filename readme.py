from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🙂 [link=https://koaning.io]Vincent D. Warmerdam", guide_style="bold bright_black")
python_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
python_tree.add("[bold link=https://scikit-lego.netlify.app/]scikit-lego[/] - [bright_black]lego bricks for sklearn")
python_tree.add("[bold link=https://koaning.github.io/human-learn/]human-learn[/] - [bright_black]rule-based components for sklearn")
python_tree.add("[bold link=https://rasahq.github.io/whatlies/]whatlies[/]    - [bright_black]word embeddings for sklearn pipelines")
python_tree.add("[bold link=https://koaning.github.io/clumper/]clumper[/]     - [bright_black]function API for lists of dicts")
python_tree.add("[bold link=https://github.com/godatadriven/evol]evol[/]        - [bright_black]grammar for genetic heuristics")
python_tree.add("[bold link=https://koaning.github.io/memo/getting-started.html]memo[/]        - [bright_black]saves a whole log of time")
python_tree.add("[bold link=https://calmcode.io/labs/drawdata.html]drawdata[/]    - [bright_black]draw datasets in jupyter")
python_tree.add("[bold link=https://github.com/koaning/tokenwiser]tokenwiser[/]  - [bright_black]sklearn token tricks via .fit_partial()")
python_tree.add("[bold link=https://github.com/koaning/mktestdocs]mktestdocs[/]  - [bright_black]turn markdown files into pytest tests")
online_tree = tree.add("⭐ Online Projects", guide_style="bright_black")
online_tree.add("[bold link=https://koaning.io]koaning.io[/]   - [bright_black]personal blog")
online_tree.add("[bold link=https://calmcode.io]calmcode.io[/]  - [bright_black]dev education service")
online_tree.add("[bold link=https://dearme.email]dearme.email[/] - [bright_black]reflection service")
talk_tree = tree.add("🎙️ Popular Talks", guide_style="bright_black")
talk_tree.add("[bold link=https://youtu.be/qcrR-Hd0LhI?t=542]Optimal Benchmarks and Other Failures[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=nJAmN6gWdK8]Playing by the Rules-Based-Systems[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=Z8MEFI7ZJlA]How to Constrain Artificial Stupidity[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=kYMfE9u-lMo]The Profession of Solving the Wrong Problem[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=68ABAU_V8qI]Winning with Simple, even Linear, Models[/]")
employer_tree = tree.add("👨‍💻 Employer", guide_style="bright_black")
employer_tree.add("[bold link=https://rasa.com]Rasa[/] - [bright_black]conversational software")


console.print(tree)
console.print("")
console.print("[green]Follow me on twitter [bold link=https://twitter.com/fishnets88]@fishnets88[/]")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
