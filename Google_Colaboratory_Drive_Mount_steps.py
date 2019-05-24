
# coding: utf-8

# ## Set Propoerties

# In[ ]:

get_ipython().system('apt-get install -y -qq software-properties-common python-software-properties module-init-tools')
get_ipython().system('add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null')
get_ipython().system('apt-get update -qq 2>&1 > /dev/null')
get_ipython().system('apt-get -y install -qq google-drive-ocamlfuse fuse')
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
get_ipython().system('google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL')
vcode = getpass.getpass()
get_ipython().system('echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}')


# ## Create a folder to serve at mount point

# In[ ]:

# Created a folder named "drive". Mounted "drive" to the google-drive folder.
get_ipython().system('mkdir -p drive')
get_ipython().system('google-drive-ocamlfuse drive')


# ## Check files and folders inside drive folder

# In[ ]:

#Here content is root folder
get_ipython().system('ls /content/drive/')


# ## Create a new directory

# In[ ]:

get_ipython().system('mkdir Test_Dir')


# ## Step to install Python Library

# In[ ]:

get_ipython().system('pip install PrettyTable')


# ## Steps to upload file from local system

# In[ ]:

from google.colab import files
uploaded = files.upload()


# ## Steps to execute an existing script, present on Google drive

# In[ ]:

get_ipython().system('python3 /content/drive/Test_Dir/<script_name>.py')

