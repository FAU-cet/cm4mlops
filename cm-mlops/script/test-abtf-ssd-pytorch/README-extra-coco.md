# Test ABTF SSD PyTorch model via CM

Install CM automation language using this [guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

Pull main repository with CM DevOps and MLOps automations

```bash
cm pull repo ctuning@mlcommons-ck
cm pull repo mlcommons@abtf-ssd-pytorch --branch=cm-automation
```

Clean CM cache if needed:

```bash
cm rm cache -f
```

Install python virtual environment to avoid messing up your original Python:

```bash
cmr "install python-venv" --name=abtf
```

Download road.jpg to your current directory:
```bash
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/road.jpg --verify=no --md5sum=470ba3b9a2f9ae21ed7a03e2680108a5
```

Test pre-trained model (add road.jpg or any other file to your current directory):
```bash
cmr "test abtf ssd-pytorch" --adr.ml-model.tags=_e65 --adr.python.name=abtf --input=road.jpg --output=road_ssd.jpg
```

# Export PyTorch model to ONNX

Export PyTorch model to ONNX:
```bash
cmr "test abtf ssd-pytorch" --adr.ml-model.tags=_e65 --adr.python.name=abtf --input=road.jpg --output=road_ssd.jpg --export_model=abtf.onnx
```

Test ONNX model with LoadGen (performance):
```bash
cm run script "python app loadgen-generic _onnxruntime" --adr.python.name=abtf --modelpath=abtf.onnx --samples=10 --quiet
```

# Misc CM commands


```bash
cmr "test abtf ssd-pytorch" --adr.ml-model.tags=_e01 --adr.python.name=abtf --input=road.jpg --output=road_ssd.jpg
```

```bash
cmr "test abtf ssd-pytorch" --adr.python.name=abtf --adr.torch.version=1.13.1 --adr.torchvision.version=0.14.1 --input=road.jpg --output=road_ssd.jpg
```

# TBD: testing docker

```bash
cm docker script --tags=test,abtf,ssd-pytorch --docker_cm_repo=ctuning@mlcommons-ck --env.CM_GH_TOKEN={TOKEN} --input=road.jpg --output=road_ssd.jpg
```

```bash
cm docker script --tags=test,abtf,ssd-pytorch --docker_cm_repo=ctuning@mlcommons-ck --docker_os=ubuntu --docker_os_version=23.04 --input=road.jpg --output=road_ssd.jpg 
```

TBD: pass file to CM docker: [meta](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml#L197).



# TBD

```bash
cmr "get dataset coco _train _2017"
cmr "get dataset coco _val _2017"

cmr "get ml-model abtf-ssd-pytorch _e65"

cmr "get mlperf inference loadgen"
```

* Automatically generate docker
  * Pass input/output files (CM has support in meta)
  * Pass git auth token for prive GitHub
* Use model from local file -> skip_if_env ...
* Add pre/post processing for COCO
* Automate training with Cognata (+ Croissant)
* Run loadgen with trained model and different devices and frameworks
* Test Croissant
* Automate multiple benchmark experiments
  * Create MLPerf-like logging and structure
* Create GUI with StreamLit