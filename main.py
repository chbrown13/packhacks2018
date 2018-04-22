import analysis
from git import *
import sys

def main():
    user = sys.argv[1]
    repo = sys.argv[2]
    try:
        Repo.clone_from("https://github.com/{user}/{repo}".replace('{user}', user).replace('{repo}', repo), repo)
    except GitCommandError:
        print 'Cloned repo already exists'
    analysis.run(repo)

if __name__ == "__main__":
    main()