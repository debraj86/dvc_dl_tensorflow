9th October lecture \
latest virtual environment for ml (tensorflow) pipeline dvc on my laptop \
>cd studyrelated\courses\mlops_ineuron\code\3_9th_oct_2021 \
create the virtual environment \
> conda create -n tensorflow-ml python=3.7 -y \
> conda activate tensorflow-ml \
install mamba for installing dvc \
>conda install -c conda-forge mamba \
>mamba install -c conda-forge dvc \
 for dvc init (use -f to forcefully initialize) \
>dvc init -f \
creating file the cmd on windows \
>type nul > dvc.yaml \
create the stage in dvc.yaml \
then execute the dvc un command \
>dvc repro \
to see the dag \
>dvc dag \
create directory config and src\utils all with a single command \
>mkdir -p config src\utils \
command to install local dependency 
>pip install -e .

