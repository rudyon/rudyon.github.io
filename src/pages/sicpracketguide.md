---
layout: '../layouts/Page.astro'
---
# Guide on setting up Racket for SICP

## Installation

Install Racket for your system of choice using the following instructions.

### Windows

#### Manually via the installer executable (Not recommended)

Go to [Racket's installer download page](https://download.racket-lang.org). Download the installer and run it. To run Racket from any folder, you need to add Racket to your system's `PATH` environment variable. Do this through System Properties -> Environment Variables, and add `C:\Program Files\Racket` to the `PATH` variable. If you’re confused about how to edit your `PATH` variable, look up a tutorial or use another method. Ideally, you shouldn't use the installer executable. If you try to use the installer and can’t figure it out yourself, feel free to ping me in the [Discord server](https://discord.gg/GkHQnHPfPf).

#### Via a Package Manager

##### Winget

Open a terminal and run `winget install --id=Racket.Racket -e` to install Racket.

#### Chocolatey

Open a terminal and run `choco install racket` to install Racket.

##### Scoop

Open a terminal and run `scoop bucket add main` to add the main bucket to Scoop (which contains Racket). After adding the bucket, run `scoop install main/racket` to install Racket.

### Unix

#### Linux

You’ll need root permissions for these commands; prefix them with `sudo` if necessary.

##### Via a Package Manager

###### Debian

Open a terminal and run `apt install racket` to install Racket.

###### Fedora

Open a terminal and run `dnf install racket` to install Racket.

###### Arch

Open a terminal and run `pacman -S racket` to install Racket.

###### Other

There are too many Linux distributions to cover here. If you’re using a distribution not listed, feel free to ping me in the [Discord server](https://discord.gg/GkHQnHPfPf).

##### Manually from source

If you’re tackling this method, you probably don’t need my help. Follow the official [guide](https://docs.racket-lang.org/racket-build-guide/build.html) for detailed instructions. If you get stuck, consider using a package manager instead.

#### MacOS

##### Manually via the installer (not recommended)

Go to [Racket's installer download page](https://download.racket-lang.org). Download the installer and run it. To run Racket from any folder, you need to add Racket to your system's `PATH` environment variable. Follow [this guide](https://beautifulracket.com/setting-the-mac-os-path.html). If you get stuck consider using Homebrew instead. You can ping me in the \[Discord server\][Discord server](https://discord.gg/GkHQnHPfPf).

##### Via Homebrew

If you don't have Homebrew install it using the instructions on the [Homebrew site](https://brew.sh). Then open a terminal and run `brew install --cask racket` to install Racket.

## Verifying the Installation

To verify that Racket installed correctly, open a terminal and run `racket --version`. If you see a `command not found` error, the installation didn’t succeed. Feel free to ping me in the [Discord server](https://discord.gg/GkHQnHPfPf) if you need help. If it’s installed correctly, you’ll see the version number.

## Setting up your editor for SICP

Pick your text/code editor of choice and follow the instructions for it. If you are using normal Vim or VI then I am sorry but I have no idea how to help you. If you are unsure about which editor to use. Then you probably want to use DrRacket.

- [ ] add info from this link here https://docs.racket-lang.org/sicp-manual/Installation.html

### DrRacket

DrRacket should have installed along with Racket. So just launch it.

### Neovim

You want to Install the Conjure plugin. Install it with your package manager using the instructions [here](https://github.com/Olical/conjure?tab=readme-ov-file#installation). If you do not have a package manager setup first set up a package manager. I recommend [Lazy](https://lazy.folke.io). If you get stuck feel free to ping me in the [Discord server](https://discord.gg/GkHQnHPfPf).

### Emacs

I can't really help you here. Since I have never used Emacs. You should probably read the official [Racket documentation](https://docs.racket-lang.org/guide/Emacs.html) on using Racket with Emacs though.

### VSCode

Install the [Magic Racket](https://marketplace.visualstudio.com/items?itemName=evzen-wybitul.magic-racket) extension and you are good to go.

## Setting up your Git repository

If you are participating in the [Discord server](https://discord.gg/GkHQnHPfPf) then you should set up a Git repository to store the solutions to your exercises. This will let you verify that you have completed the book which will grant you the `@Knight` role on the [Discord server](https://discord.gg/GkHQnHPfPf). If you are not participating in the Discord I still highly recommend you do this. However despite my recommendations this step is still optional.

### Installing Git

First you will need to install Git. I will not be giving instructions on how to install Git. Since I already have given instructions on installing Racket and Git's installation process is very similar. If you are on Windows or MacOS and don't want to use a package manager for some reason go to [Git's download page](https://git-scm.com/downloads) to get the installer. If you are using a package manager it should be as simple as typing the same command you used to install Racket but replacing `racket` with `git`.

### Initializing the repository

After installing Git you can then setup your Git repository. Open a new folder wherever you want and name it `sicp`. Open a terminal inside the folder (or go to the folder using `cd`). Then run `git init`. This will initiate your Git repository.

### Creating a Github repository

Now that you have your local repository, it's time to push it to GitHub. If you don’t have a GitHub account, create one at [GitHub.](https://github.com/). Once you're signed in, create a new repository named `sicp`.

Next, you’ll want to link your local repository to GitHub. In your terminal, run:

```bash
git remote add origin https://github.com/<username>/sicp.git
git branch -M main
git push -u origin main
```

Replace `<username>` with your GitHub username, obviously.

### Committing your work

Whenever you solve an exercise or make some progress, you should commit your changes. Run the following commands:

```bash
git add .
git commit -m "Completed Exercise X.Y"
git push
```

This way, your work is safely stored online, and you can easily track your progress. Plus, when you finish the book, you’ll have a record of all your hard work.

Feel free to ping me on the [Discord server](https://discord.gg/GkHQnHPfPf) if you run into any issues!

## Making Racket compatible with SICP

Racket is different from SICP's Scheme. However Racket comes with support for SICP out of the box. This is the reason I recommend Racket. Whenever you make a new Racket file put `#lang sicp` on the first line. This will tell Racket to make itself compatible with the book.