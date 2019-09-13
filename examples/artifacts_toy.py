from time import sleep

import pandas as pd
import numpy as np
from PIL import Image
from trains import Task

task = Task.init('examples', 'artifacts toy')

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])

# register Pandas object as artifact to watch
# (it will be monitored in the background and automatically synced and uploaded)
task.register_artifact('train', df, metadata={'counting': 'legs', 'max legs': 69})
# change the artifact object
df.sample(frac=0.5, replace=True, random_state=1)
# or access it from anywhere using the Task
Task.current_task().artifacts['train'].sample(frac=0.5, replace=True, random_state=1)

# add and upload local file artifact
task.upload_artifact('local file', artifact_object='samples/dancing.jpg')
# add and upload dictionary stored as JSON)
task.upload_artifact('dictionary', df.to_dict())
# add and upload Numpy Object (stored as .npz file)
task.upload_artifact('Numpy Eye', np.eye(100, 100))
# add and upload Image (stored as .png file)
im = Image.open('samples/dancing.jpg')
task.upload_artifact('pillow_image', im)

# do something
sleep(1.)
print(df)

# we are done
print('Done')