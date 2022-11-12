# Если не запускается

При ошибке NotImplementedError: Platform does not define a GLUT font retrieval function, прописать в терминале:

$ sudo apt-get install libosmesa6
$ export PYOPENGL_PLATFORM=osmesa
