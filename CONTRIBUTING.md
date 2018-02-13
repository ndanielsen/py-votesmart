# Contributing to Py-votesmart

## How to Contribute

Py-votesmart is an open source project that is supported by a community who will gratefully and humbly accept any contributions you might make to the project. Large or small, any contribution makes a big difference; and if you've never contributed to an open source project before, you're more than welcome.

Principally, Py-votesmart development is about supporting the Project Vote Smart API and making it easier for organizations to access it's data.

There are many ways to contribute:

* Submit a bug report or feature request on GitHub Issues.
* Contribute a Jupyter notebook to our examples gallery.
* Add to the documentation.
* Write unit or integration tests for our project.

As you can see, there are lots of ways to get involved and we would be very happy for you to join us! The only thing we ask is that you abide by the principles of openness, respect, and consideration of others as described in the [Python Software Foundation Code of Conduct](https://www.python.org/psf/codeofconduct/).

## Signing up for a Project Votesmart API Key

Votesmart is a non-profile and it requires you to make a small contribution in most cases to access it's API.

As py-votesmart is an interface for the Votesmart API, you'll need to [signup for an account](https://votesmart.org/login#signup) and request an API key.

After signing up, click on 'User Panel' in the upper right hand corner.
Application Programming Interface. You'll be asked a series of questions.

## Getting Started on GitHub

Py-votesmart is hosted on GitHub at https://github.com/ndanielsen/py-votesmart.

The typical workflow for a contributor to the codebase is as follows:

1. **Discover** a bug or a feature by using py-votesmart.
2. **Discuss** with the core contributes by [adding an issue](https://github.com/ndanielsen/py-votesmart/issues).
3. **Assign** yourself the task by pulling a task from our [Issues page](https://github.com/ndanielsen/py-votesmart/issues).
4. **Fork** the repository into your own GitHub account.
5. Create a **Pull Request** first thing to [connect with us](https://github.com/ndanielsen/py-votesmart/pulls) about your task.
6. **Code** the feature, write the documentation, add your contribution.
7. **Review** the code with core contributors who will guide you to a high quality submission.
8. **Merge** your contribution into the py-votesmart codebase.

**Note**: Create a pull request as soon as possible, even before you've started coding. This will allow the core contributors to give you advice about where to add your code or utilities and discuss other style choices and implementation details as you go. Don't wait!

We believe that _contribution is collaboration_ and therefore emphasize _communication_ throughout the open source process. We rely heavily on GitHub's social coding tools to allow us to do this.

### Forking the Repository

The first step is to fork the repository into your own account. This will create a copy of the codebase that you can edit and write to. Do so by clicking the **"fork"** button in the upper right corner of the Py-Votesmart GitHub page.

Once forked, use the following steps to get your development environment set up on your computer:

1. Clone the repository.

   After clicking the fork button, you should be redirected to the GitHub page of the repository in your user account. You can then clone a copy of the code to your local machine.

   `$ git clone https://github.com/[YOURUSERNAME]/py-votesmart $ cd py-votesmart`

2. Create a virtual environment.

   Py-votesmart developers typically use [virtualenv](https://virtualenv.pypa.io/en/stable/) (and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [pyenv](https://github.com/pyenv/pyenv-virtualenv) or [conda envs](https://conda.io/docs/using/envs.html) in order to manage their Python version and dependencies. Using the virtual environment tool of your choice, create one for py-votesmart. Here's how with virtualenv:

   `$ virtualenv venv`

3. Install dependencies.

   Py-votesmart's dependencies are in the `requirements.txt` document at the root of the repository. Open this file and uncomment the dependencies that are for development only. Then install the dependencies with `pip`:

   `$ pip install -r requirements.txt`

   Note that there may be other dependencies required for development and testing, you can simply install them with `pip`.

4. Switch to the develop branch.

   The Py-votesmart repository has a `develop` branch that is the primary working branch for contributions. It is probably already the branch you're on, but you can make sure and switch to it as follows::

   `$ git fetch $ git checkout develop`

At this point you're ready to get started writing code. If you're going to take on a specific task, we'd strongly encourage you to check out the issue on the [Issue's Page](https://github.com/ndanielsen/py-votesmart/issues) and create a [pull request](https://github.com/ndanielsen/py-votesmart/pulls) **before you start coding** to better foster communication with other contributors.

### Branching Conventions

The Py-votesmart repository is set up in a typical production/release/development cycle as described in "[A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/)>." The primary working branch is the `develop` branch. This should be the branch that you are working on and from, since this has all the latest code. The `master` branch contains the latest stable version and release*, which is pushed to PyPI*. No one but core contributors will generally push to master.

**NOTE:** All pull requests should be into the `py-votesmart/develop` branch from your forked repository.

You can work directly in your fork and create a pull request from your fork's develop branch into ours. We also recommend setting up an `upstream` remote so that you can easily pull the latest development changes from the main Py-votesmart repository (see [configuring a remote for a fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/)). You can do that as follows:

`$ git remote add upstream https://github.com/ndanielsen/py-votesmart.git`
`$ git remote -v`

> origin https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
> upstream https://github.com/ndanielsen/py-votesmart.git (fetch)
> upstream https://github.com/ndanielsen/py-votesmart.git (push)

When you're ready, request a code review for your pull request. Then, when reviewed and approved, you can merge your fork into our main branch. Make sure to use the "Squash and Merge" option in order to create a Git history that is understandable.

**NOTE**: When merge a pull request, use the "squash and merge" option.

Core contributors have write access to the repository. In order to reduce the number of merges (and merge conflicts) we recommend that you utilize a feature branch off of develop to do intermediate work in::

    $ git checkout -b feature-myfeature develop

Once you are done working (and everything is tested) merge your feature into develop.::

    $ git checkout develop
    $ git merge --no-ff feature-myfeature
    $ git branch -d feature-myfeature
    $ git push origin develop

Head back to the Issue page and checkout another issue!
