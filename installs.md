
# Python install setup for SUSE linux

```sh
# install zsh
sudo zypper install zsh
sudo zypper install stow

# install build tools https://bobbyhadz.com/blog/configure-error-no-acceptable-c-compiler-found-in-path#:~:text=The%20error%20%22Configure%20error%3A%20no,and%20present%20in%20your%20%24PATH%20.
sudo zypper install --type pattern devel_basis
sudo zypper install gcc automake bzip2 libbz2-devel xz xz-devel openssl-devel ncurses-devel \
readline-devel zlib-devel tk-devel libffi-devel sqlite3-devel gdbm-devel make findutils patch

# Install mise to manage python installs and other versions (node, etc)
curl https://mise.jdx.dev/install.sh | sh

# Set mise to run in zsh
echo 'eval "$(mise activate zsh)"' >> "${ZDOTDIR-$HOME}/.zshrc"
mise settings set python_compile 1
```

# Ubuntu Linux

```sh
# install zsh
sudo apt install zsh
sudo apt install stow

# install build tools https://bobbyhadz.com/blog/configure-error-no-acceptable-c-compiler-found-in-path#:~:text=The%20error%20%22Configure%20error%3A%20no,and%20present%20in%20your%20%24PATH%20.
sudo apt install --type pattern devel_basis
sudo apt install gcc automake bzip2 libbz2-devel xz xz-devel openssl-devel ncurses-devel \
readline-devel zlib-devel tk-devel libffi-devel sqlite3-devel gdbm-devel make findutils patch

# Install mise to manage python installs and other versions (node, etc)
curl https://mise.jdx.dev/install.sh | sh

# Set mise to run in zsh by copying this to .zshrc
~/.local/bin/mise activate zsh

mise settings set python_compile 1
```