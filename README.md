#django


### やったこと

### pyenv install anaconda3-5.2.0

### pyenv versions

### pyenv global anaconda3-5.2.0

### vim ~/dotfiles2/.zshrc

```
# 順番重要
# pyenv
eval "$(pyenv init -)"
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# anaconda
export PATH="$PYENV_ROOT/versions/anaconda3-5.2.0/bin/:$PATH"
```
### source ~/dotfiles2/.zshrc

### conda update conda

### conda create -n py36

### source activate py36

### source deactivate py36

### 参照

- [pyenv + anacondaをインストールした](https://nekodeki.com/pyenv-anaconda%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%9F/)
