from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🙂 [link=https://koaning.io]Vincent D. Warmerdam", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
python_tree.add("[bold link=https://github.com/koaning/doubtlab]doubtlab[/]       - [bright_black]suite of tools to find bad labels")
python_tree.add("[bold link=https://github.com/koaning/scikit-lego]scikit-lego[/]    - [bright_black]lego bricks for sklearn")
python_tree.add("[bold link=https://github.com/koaning/scikit-partial]scikit-partial[/] - [bright_black]partial_fit() pipelines for sklearn")
python_tree.add("[bold link=https://github.com/koaning/embetter]embetter[/]       - [bright_black]embeddings ready for sklearn")
# python_tree.add("[bold link=https://koaning.github.io/scikit-bloom/]scikit-bloom[/]   - [bright_black]bloom transformers for sklearn")
python_tree.add("[bold link=https://github.com/koaning/human-learn]human-learn[/]    - [bright_black]rule-based components for sklearn")
python_tree.add("[bold link=https://github.com/koaning/icepickle]icepickle[/]      - [bright_black]cool and safe storage for linear models")
python_tree.add("[bold link=https://github.com/koaning/drawdata]drawdata[/]       - [bright_black]draw datasets in jupyter")
python_tree.add("[bold link=https://github.com/koaning/clumper]clumper[/]        - [bright_black]functional API for lists of dicts")
python_tree.add("[bold link=https://github.com/koaning/mktestdocs]mktestdocs[/]     - [bright_black]turn markdown files into pytest tests")
python_tree.add("[bold link=https://github.com/koaning/skedulord]skedulord[/]      - [bright_black]makes cron a bit more fun")
python_tree.add("[bold link=https://github.com/koaning/memo]memo[/]           - [bright_black]saves a whole log of time")
python_tree.add("[bold link=https://github.com/koaning/pytest-duration-insights]durations[/]      - [bright_black]pytest duration insights")
python_tree.add("[bold link=https://github.com/koaning/justcharts]justcharts.js[/]  - [bright_black]hosting vegalite charts, just easier")
python_tree.add("[bold link=https://github.com/godatadriven/evol]evol[/]           - [bright_black]grammar for genetic heuristics")

contrib_tree = tree.add("🔬 Experiments", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/pola-rs/valves]valves[/]         - [bright_black]general .pipe()-lines")
contrib_tree.add("[bold link=https://github.com/koaning/akin]akin[/]           - [bright_black]sort based on zero-shot similarities")
contrib_tree.add("[bold link=https://github.com/koaning/tjek]tjek[/]           - [bright_black]tjek changes with the main branch")
contrib_tree.add("[bold link=https://github.com/koaning/gitlit]gitlit[/]         - [bright_black]tracking github action times across open source")
contrib_tree.add("[bold link=https://github.com/koaning/sentimany]sentimany[/]      - [bright_black]many sentiment models, one repo")
contrib_tree.add("[bold link=https://github.com/koaning/simsity]simsity[/]        - [bright_black]a super simple similarities service")
contrib_tree.add("[bold link=https://github.com/koaning/scikit-teach/]scikit-teach[/]   - [bright_black]some active learning benchmarks")
contrib_tree.add("[bold link=https://github.com/koaning/tokenwiser]tokenwiser[/]     - [bright_black]sklearn token tricks")
contrib_tree.add("[bold link=https://github.com/koaning/benchmarks]benchmarks[/]     - [bright_black]some random, but intersting, benchmarks")
python_tree.add("[bold link=https://github.com/koaning/whatlies]whatlies[/]       - [bright_black]word embeddings for sklearn pipelines")

contrib_tree = tree.add("👍 Contributions", guide_style="bright_black")
contrib_tree.add("[bold link=https://fairlearn.org/v0.7.0/api_reference/fairlearn.preprocessing.html#fairlearn.preprocessing.CorrelationRemover]fairlearn[/]      - [bright_black]contributed the CorrelationFilter")

online_tree = tree.add("⭐ Online Projects", guide_style="bright_black")
online_tree.add("[bold link=https://koaning.io]koaning.io[/]     - [bright_black]personal blog")
online_tree.add("[bold link=https://calmcode.io]calmcode.io[/]    - [bright_black]dev education service")
online_tree.add("[bold link=https://dearme.email]dearme.email[/]   - [bright_black]reflection service")

talk_tree = tree.add("🎙️ Popular Talks", guide_style="bright_black")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=lJKPiOf_o8k]Optimal on Paper, Broken in Reality[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=nJAmN6gWdK8]Playing by the Rules-Based-Systems[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=Z8MEFI7ZJlA]How to Constrain Artificial Stupidity[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=kYMfE9u-lMo]The Profession of Solving the Wrong Problem[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=68ABAU_V8qI]Winning with Simple, even Linear, Models[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=yXGCKqo5cEY]Untitled12.ipynb[/]")

employer_tree = tree.add("👨‍💻 Employer", guide_style="bright_black")

explosion_tree = employer_tree.add("[bold link=https://explosion.ai/]💥 Explosion[/]  - [bright_black]developer tools for ml")
explosion_tree.add("[bold link=https://github.com/koaning/bulk]bulk[/]          - [bright_black]simple bulk labelling interface")
explosion_tree.add("[bold link=https://github.com/koaning/cluestar]cluestar[/]      - [bright_black]inspiration for your first text labels")
explosion_tree.add("[bold link=https://github.com/koaning/spacy-report]spacy-report[/]  - [bright_black]reports for spaCy models")

rasa_tree = employer_tree.add("[bold link=https://rasa.com]🤖 Rasa[/]       - [bright_black]conversational software")
rasa_tree.add("[bold link=https://github.com/RasaHQ/rasa-nlu-examples]nlu examples[/]      - [bright_black]custom nlu components for Rasa")
rasa_tree.add("[bold link=https://github.com/RasaHQ/taipo]taipo[/]             - [bright_black]data augmentation tools")
rasa_tree.add("[bold link=https://www.youtube.com/watch?v=wWNMST6t1TA&list=PL75e0qA87dlG-za8eLI6t0_Pbxafk-cxb]algo whiteboard [/]  - [bright_black]nlp education")

console.print(tree)
console.print("")
console.print("[green]Follow me on twitter [bold link=https://twitter.com/fishnets88]@fishnets88[/]")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
