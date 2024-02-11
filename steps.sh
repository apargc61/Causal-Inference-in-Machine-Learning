  573  git clone https://github.com/apargc61/Causal-Inference-in-Machine-Learning.git
  574  git branch
  575  git checkout -b "DropsChecking"
  576  git status
  577  cd Causal-Inference-in-Machine-Learning
  578  git checkout -b "dropCheck"
  579  python -m venv venv
  580  venv/source/activate
  581  ls
  582  source venv/bin/activate
  583  pip install jupyterlab
  584  pip install ipykernel
  585  python -m ipykernel install --user --name=venv
  586  jupyter lab