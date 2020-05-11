import json
from argparse import ArgumentParser
from requests import Session


def make_github_issue(repo_owner,
                      repo_name,
                      username,
                      personal_token,
                      title,
                      body,
                      labels=[]):
    '''
    Create an issue on github.com using the given parameters
    
    Source:
    -------
        https://gist.github.com/JeffPaine/3145490#gistcomment-2226141
    '''
    
    # Create an authenticated session to create the issue
    session      = Session()
    session.auth = (username, personal_token)
    
    params = {'title':  title,
              'body':   body,
              'labels': labels}
    
    template_url = 'https://api.github.com/repos/{owner}/{name}/issues'
    url          = template_url.format(owner=repo_owner,
                                       name=repo_name)
    
    # Add the issue to our repository
    r = session.post(url, json.dumps(params))
    
    if r.status_code == 201:
        print('Successfully created Issue {0:s}'.format(title))
    else:
        print('Could not create Issue {0:s}\n'.format(title))
        print('Response: {}\n'.format(r.content))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-u', dest='user_name',      help='Username')
    parser.add_argument('-t', dest='personal_token', help='Personal Token')
    parser.add_argument('-r', dest='repo',           help='Repo Name')
    args = parser.parse_args()
    
    user  = str(args.user_name)
    token = str(args.personal_token)
    repo  = str(args.repo)
    
    print('Username: {}'.format(user))
    print('Personal Token: {}'.format(token))
    print('Repo Name: {}'.format(repo))
    
    make_github_issue(repo_owner='arduino',
                      repo_name='Arduino',
                      username=user,
                      personal_token=token,
                      title='[Library Manager] Add library {}'.format(repo),
                      body='Please add https://github.com/{}/{}\n\nThank you!'.format(user, repo),
                      labels=['Component: Board/Lib Manager'])