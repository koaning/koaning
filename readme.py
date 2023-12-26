from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🙂 [link=https://koaning.io]Vincent D. Warmerdam", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
python_tree.add("[bold link=https://github.com/koaning/bulk]bulk[/]              - [bright_black]simple bulk labelling interface")
python_tree.add("[bold link=https://github.com/koaning/embetter]embetter[/]          - [bright_black]embeddings ready for sklearn")
python_tree.add("[bold link=https://github.com/koaning/doubtlab]doubtlab[/]          - [bright_black]suite of tools to help find bad labels")
python_tree.add("[bold link=https://github.com/koaning/scikit-lego]scikit-lego[/]       - [bright_black]lego bricks for sklearn")
python_tree.add("[bold link=https://github.com/koaning/scikit-partial]scikit-partial[/]    - [bright_black]partial_fit() pipelines for sklearn")
python_tree.add("[bold link=https://github.com/koaning/scikit-prune/]scikit-prune[/]      - [bright_black]prune scikit learn pipelines")
python_tree.add("[bold link=https://github.com/koaning/scikit-bloom/]scikit-bloom[/]      - [bright_black]bloom transformers for sklearn")
python_tree.add("[bold link=https://github.com/koaning/human-learn]human-learn[/]       - [bright_black]rule-based components for sklearn")
python_tree.add("[bold link=https://github.com/koaning/sentence-models]sentence-models[/]   - [bright_black]a different take on textcat")
python_tree.add("[bold link=https://github.com/koaning/mktestdocs]mktestdocs[/]        - [bright_black]turn markdown files into pytest tests")
python_tree.add("[bold link=https://github.com/koaning/lazylines]lazylines[/]         - [bright_black]lightweight utils for .jsonl wrangling")
python_tree.add("[bold link=https://github.com/koaning/cluestar]cluestar[/]          - [bright_black]inspiration for your first text labels")
python_tree.add("[bold link=https://github.com/koaning/drawdata]drawdata[/]          - [bright_black]draw datasets in jupyter")
python_tree.add("[bold link=https://github.com/koaning/pytest-duration-insights]durations[/]         - [bright_black]pytest duration insights")
python_tree.add("[bold link=https://github.com/koaning/tuilwindcss]tuilwindcss[/]       - [bright_black]tailwindcss for textual tui apps")
python_tree.add("[bold link=https://github.com/koaning/memo]memo[/]              - [bright_black]saves a whole log of time")
python_tree.add("[bold link=https://github.com/koaning/skedulord]skedulord[/]         - [bright_black]makes cron a bit more fun")
python_tree.add("[bold link=https://github.com/koaning/icepickle]icepickle[/]         - [bright_black]cool and safe storage for linear models")
python_tree.add("[bold link=https://github.com/godatadriven/evol]evol[/]              - [bright_black]grammar for genetic heuristics")


contrib_tree = tree.add("👍 Project Contributions", guide_style="bright_black")
contrib_tree.add("[bold link=https://fairlearn.org/v0.7.0/api_reference/fairlearn.preprocessing.html#fairlearn.preprocessing.CorrelationRemover]fairlearn[/]         - [bright_black]contributed the CorrelationFilter")
contrib_tree.add("[bold link=https://github.com/pola-rs/polars/pull/82]polars[/]            - [bright_black]contributed the .pipe() method")
contrib_tree.add("[bold link=https://github.com/MaartenGr/BERTopic/issues/768]BERTopic[/]          - [bright_black]added lightweight sklearn pipeline support")

online_tree = tree.add("⭐ Online Projects", guide_style="bright_black")
online_tree.add("[bold link=https://koaning.io]koaning.io[/]        - [bright_black]personal blog")
online_tree.add("[bold link=https://calmcode.io]calmcode.io[/]       - [bright_black]intermediate developer education")
online_tree.add("[bold link=https://dearme.email]dearme.email[/]      - [bright_black]reflection via a 30 day delay")

talk_tree = tree.add("🎙️ Popular Talks", guide_style="bright_black")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=C9p7suS-NGk]Natural Intelligence is All You Need[tm][/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=S7vhi6RjBZA]Group-by statements that save the day[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=KRQJDLyc1uM]Tools to Improve Training Data[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=lJKPiOf_o8k]Optimal on Paper, Broken in Reality[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=nJAmN6gWdK8]Playing by the Rules-Based-Systems[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=Z8MEFI7ZJlA]How to Constrain Artificial Stupidity[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=kYMfE9u-lMo]The Profession of Solving the Wrong Problem[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=68ABAU_V8qI]Winning with Simple, even Linear, Models[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=yXGCKqo5cEY]Untitled12.ipynb[/]")

experiments_tree = tree.add("🔬 Random Experiments", guide_style="bright_black")
python_tree.add("[bold link=https://github.com/koaning/simsity]simsity[/]           - [bright_black]a super simple similarities service")
experiments_tree.add("[bold link=https://github.com/koaning/gitlit]gitlit[/]         - [bright_black]tracking github action times across open source")
experiments_tree.add("[bold link=https://github.com/koaning/sentimany]sentimany[/]      - [bright_black]many sentiment models, one repo")
experiments_tree.add("[bold link=https://github.com/koaning/tokenwiser]tokenwiser[/]     - [bright_black]sklearn token tricks")
experiments_tree.add("[bold link=https://github.com/koaning/clumper]clumper[/]        - [bright_black]functional API for lists of dicts")
experiments_tree.add("[bold link=https://github.com/koaning/whatlies]whatlies[/]       - [bright_black]exploration tools for word embeddings")

employer_tree = tree.add("👨‍💻 Employer", guide_style="bright_black")

explosion_tree = employer_tree.add("[bold link=https://explosion.ai/]💥 Explosion[/]   - [bright_black]developer tools for nlp")
explosion_tree.add("[bold link=https://github.com/koaning/prodigy-hf]prodigy-hf[/]        - [bright_black]Prodigy integration for the HuggingFace stack")
explosion_tree.add("[bold link=https://github.com/koaning/prodigy-pdf]prodigy-pdf[/]       - [bright_black]Annotate PDFs via Prodigy")
explosion_tree.add("[bold link=https://github.com/koaning/prodigy-ann]prodigy-ann[/]       - [bright_black]ANN techniques to find relevant subsets")
explosion_tree.add("[bold link=https://github.com/koaning/prodigy-segment]prodigy-segment[/]   - [bright_black]Prodigy integration for Segment Anything")
explosion_tree.add("[bold link=https://github.com/koaning/prodigy-lunr]prodigy-lunr[/]      - [bright_black]Search techniques to find relevant subsets")
explosion_tree.add("[bold link=https://github.com/explosion/prodigy-whisper]prodigy-whisper[/]   - [bright_black]Transcribe audio with OpenAI's whisper models")
explosion_tree.add("[bold link=https://github.com/koaning/prodigy-tui]prodigy-tui[/]       - [bright_black]Prodigy from the terminal")
explosion_tree.add("[bold link=https://github.com/koaning/cluestar]cluestar[/]          - [bright_black]inspiration for your first text labels")

rasa_tree = employer_tree.add("[bold link=https://rasa.com]🤖 Rasa[/]        - [bright_black]conversational software provider")
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
