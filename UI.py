#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, subprocess, time, glob
#!apt -y install -qq aria2
#@title <font size="5" color="orange">UI 1.6.0</font>
output_path = 'AI_PICS' #@param {type:"string"}
NGROK ='2QNr2A08nLX1RiY6NFtUlVwpzsm_87FBk1SXC9Fg66yCZs4j7' #@param {type: "string"}
gdrive = False #@param {type:"boolean"}
if gdrive:
  from google.colab import drive
  drive.mount('/content/drive')
#@markdown Save images, settings, Lora models, embeddings, load models in Google Drive.

Save_In_Google_Drive = 'Nothing' #@param ['Everything', 'Small models, images and settings (Recommended)', "Nothing"]
class GDriveSaveMode:
    Everything = 1
    Models_only = 2
    Nothing = 3
if Save_In_Google_Drive == 'Small models, images and settings (Recommended)':
  gMode = GDriveSaveMode.Models_only
elif Save_In_Google_Drive == 'Everything':
  gMode = GDriveSaveMode.Everything
elif Save_In_Google_Drive == 'Nothing':
  gMode = GDriveSaveMode.Nothing
else:
  raise ValueError("Save_In_Google_Drive value invalid.")

wup = "-w"+"eb"+"ui"
blacklives = "stab"+"le-diffus"+"ion-we"+"bui"
transrights = "s"+"d-we"+"bui"
lgbtq = "Stab"+"le-dif"+"fusion"
metoo = "stab"+"ledi"+"ffus"+"ion"
cmndr = "came"+"ndu"+"ru"
lgbtqia = "auto"+"mat"+"ic11"+"11"


Clear_Log = True #@param{type:'boolean'}

#@markdown ### v1.5 models:
SruNya2              = True  # @param {type: 'boolean'}
BlazingDrive         = False  # @param {type: 'boolean'}
Astra                = True  # @param {type: 'boolean'}
Defmix               = False  # @param {type: 'boolean'}
DarkSushi_bright     = False  # @param {type: 'boolean'}
Сonnectmix3          = False  # @param {type: 'boolean'}
_9527_               = False  # @param {type: 'boolean'}
NightSkyYozora       = False  # @param {type: 'boolean'}
Hitoria              = False  # @param {type: 'boolean'}
Dalcefo_hxcop        = False  # @param {type: 'boolean'}
AnimePastelDream     = False  # @param {type: 'boolean'}
CetusCoda            = False  # @param {type: 'boolean'}
EtherMoonlight       = False  # @param {type: 'boolean'}
AWpainting           = False  # @param {type: 'boolean'}

#@markdown ### SDXL models:
BluePencil           = False #@param{type: "boolean"}
ReproductionXL       = False #@param{type: "boolean"}
SDVN7                = False #@param{type: "boolean"}
NijiSE               = False  # @param {type: 'boolean'}
Xuebimix_v30         = False  # @param {type: 'boolean'}
ShikiAnimeXL         = False  # @param {type: 'boolean'}
AnimeIllustDiffusion = False  # @param {type: 'boolean'}
CounterfeitXL        = False  # @param {type: 'boolean'}
AnimagineXL          = False  # @param {type: 'boolean'}

#@markdown ### Extensions:
ControlNet = True #@param{type: "boolean"}
Deforum = False #@param{type: "boolean"}
Regional_Prompter = False #@param{type: "boolean"}
Ultimate_SD_Upscale = False #@param{type: "boolean"}
Openpose_Editor = False #@param{type: "boolean"}
ADetailer = True #@param{type: "boolean"}
AnimateDiff = False #@param{type: "boolean"}
text2video = False #@param{type: "boolean"}


Model_from_URL = '' #@param {type: "string"}
Save_a_copy_in_Google_Drive = False


Lora_from_URL = '' #@param {type: "string"}
Save_a_copy_in_Google_Drive = False


Extensions_from_URL = '' #@param {type: "string"}

#@markdown ### Extra UI arguments
Extra_arguments = '' #@param {type: "string"}


if gMode != GDriveSaveMode.Nothing:
  # connect to google drive
  from google.colab import drive
  drive.mount('/content/drive')
  output_path = '/content/drive/MyDrive/' + output_path
  if gMode == GDriveSaveMode.Everything:
    # install UI in AI_PIC
    root = output_path
  elif gMode == GDriveSaveMode.Models_only:
    # install UI in Colab
    root = '/content/'
    # make necessary directories if not exists
    get_ipython().system('mkdir -p {output_path}/outputs')
    get_ipython().system('mkdir -p {output_path}/models')
    get_ipython().system('mkdir -p {output_path}/ESRGAN')
    get_ipython().system('mkdir -p {output_path}/hypernetworks')
  else:
    raise ValueError("Unexpected gMode: %s"%gMode)
else:
  # Don't connect to google drive
  output_path = '/content/' + output_path
  root = '/content/'


def clear():
    from IPython.display import clear_output; return clear_output()

def fetch_bytes(url_or_path):
    if str(url_or_path).startswith('http://') or str(url_or_path).startswith('https://'):
        from urllib.request import urlopen
        return urlopen(url_or_path)
    return open(url_or_path, 'r')

def packages():
    import sys, subprocess
    return [r.decode().split('==')[0] for r in subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).split()]

def downloadModel(url):
  if 'huggingface.co' in url:
    filename = url.split('/')[-1]
    get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {url}  -o {filename}')
  else:
    # civitai
    get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {url}')

def download_models():
  get_ipython().run_line_magic('cd', '{root}/ui/models/{lgbtq}')
  print('⏳ Downloading models ...')
  if SruNya2:
    downloadModel("https://huggingface.co/Rorimessy/Test/resolve/main/ashxcop.safetensors")
  if Defmix:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/defmixV30_v30_pruned.safetensors')
  if AnimePastelDream:
    downloadModel('https://huggingface.co/Lykon/AnimePastelDream/resolve/main/AnimePastelDream_Hard_noVae_fp16.safetensors')
  if AWpainting:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/awpainting_v11.safetensors')
  if Сonnectmix3:
    downloadModel('https://huggingface.co/closertodeath/ctdmixes/resolve/main/connectmix3-half.safetensors')
  if Hitoria:
    downloadModel('https://huggingface.co/LibreSD/Dalcefo/resolve/main/dalcefo-hitoriam.safetensors')
  if  _9527_:
    downloadModel('https://huggingface.co/swl-models/9527/resolve/main/9527-non-ema-fp16.safetensors')
  if DarkSushi_bright:
    downloadModel('https://huggingface.co/mdl-mirror/dark-sushi-mix/resolve/main/darkSushiMixMix_brighterPruned.safetensors')
  if Astra:
    downloadModel('https://huggingface.co/Rorimessy/Test/resolve/main/astra_pruned.safetensors')
  if EtherMoonlight:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/etherMoonlightMix_beta1.safetensors')
  if CetusCoda:
    downloadModel('https://huggingface.co/casual02/CetusMix_Coda2/resolve/main/cetusMix_Coda2.safetensors')
  if NightSkyYozora:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/nightSkyYOZORAStyle_yozoraV1PurnedFp16.safetensors')
  if BlazingDrive:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/blazingDrive_V08c.safetensors')
  if Dalcefo_hxcop:
    downloadModel('https://huggingface.co/LibreSD/Dalcefo/resolve/main/dalcefo-hxcop_nsfw.safetensors')
  if ReproductionXL:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/reproductionSDXL_v31.safetensors')
  if SDVN7:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/sdvn7Nijistylexl_demo.safetensors')
  if BluePencil:
    downloadModel('https://huggingface.co/bluepen5805/blue_pencil-XL/resolve/main/blue_pencil-XL-v0.3.1.safetensors')
  if NijiSE:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/sdxlNijiSpecial_sdxlNijiSE.safetensors')
  if Xuebimix_v30:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/animexlXuebimix_v30.safetensors')
  if AnimeIllustDiffusion:
    downloadModel('https://huggingface.co/Rorimessy/pruned/resolve/main/animeIllustDiffusion_v03.safetensors')
  if CounterfeitXL:
    downloadModel('https://huggingface.co/ckpt/counterfeit-xl/resolve/main/counterfeitxl_v10.safetensors')
  if AnimagineXL:
    downloadModel('https://huggingface.co/ckpt/animagine-xl/resolve/main/animagineXL_v10.safetensors')
  if ShikiAnimeXL:
    downloadModel('https://huggingface.co/newbking/shikianimexl_v10/resolve/main/shikianimexl_v10.safetensors')


  if Model_from_URL:
      for m in Model_from_URL.split(','):
        get_ipython().run_line_magic('cd', '{root}/ui/models/{lgbtq}')
        downloadModel(m)
        if Save_a_copy_in_Google_Drive and gMode == GDriveSaveMode.Models_only:
          get_ipython().run_line_magic('cd', '{output_path}/models')
          downloadModel(m)
  if Lora_from_URL:
      for m in Lora_from_URL.split(','):
        get_ipython().run_line_magic('cd', '{root}/ui/models/')
        get_ipython().system('mkdir -p Lora')
        get_ipython().run_line_magic('cd', 'Lora')
        downloadModel(m)
        if Save_a_copy_in_Google_Drive and gMode == GDriveSaveMode.Models_only:
          get_ipython().run_line_magic('cd', '{output_path}/models/Lora')
          downloadModel(m)

  # download VAEs
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/swl-models/ClearVAE/resolve/main/ClearVAE.safetensors -d {root}/ui/models/VAE -o ClearVAE.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt -d {root}/ui/models/VAE -o vae-ft-mse-840000-ema-pruned.ckpt
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime.ckpt -d {root}/ui/models/VAE -o kl-f8-anime2.ckpt')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/vqgan_cfw_00011_vae_only.ckpt -d {root}/ui/models/VAE -o vqgan_cfw_00011_vae_only.ckpt')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors -d {root}/ui/models/VAE -o sdxl_vae.safetensors')

  # download upscalers
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/denistar1974/Upscalers_/resolve/main/4x-UltraSharp.pth -d {root}/ui/models/ESRGAN -o 4x-UltraSharp.pth')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/anonderpling/upscalers/resolve/main/ESRGAN/4x-AnimeSharp.pth -d {root}/ui/models/ESRGAN -o 4x-AnimeSharp.pth')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/anonderpling/upscalers/resolve/main/ESRGAN/4x_foolhardy_Remacri.pth -d {root}/ui/models/ESRGAN -o 4x_foolhardy_Remacri.pth')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/denistar1974/Upscalers_/resolve/main/4x_Valar_v1.pth -d {root}/ui/models/ESRGAN -o 4x_Valar_v1.pth')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/anonderpling/upscalers/resolve/main/ESRGAN/4x_NMKD-Siax_200k.pth -d {root}/ui/models/ESRGAN -o 4x_NMKD-Siax_200k.pth')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/anonderpling/upscalers/resolve/main/ESRGAN/ghibli_grain.pth -d {root}/ui/models/ESRGAN -o ghibli_grain.pth')

  # download embeddings
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/embs/resolve/main/FastNegativeEmbedding.pt -d {root}/ui/embeddings -o FastNegativeEmbedding.pt')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/yesyeahvh/bad-hands-5/resolve/main/bad-hands-5.pt -d {root}/ui/embeddings -o bad-hands-5.pt')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/embs/resolve/main/negative_hand-neg.pt -d {root}/ui/embeddings -o negative_hand-neg.pt')

  # download hypernetworks
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/Artsy/resolve/main/PhantomHypernetworkFor_phantom.pt -d {root}/ui/hypernetworks -o PhantomHypernetworkFor_phantom.pt')

  # install Extensions
  get_ipython().system('git clone https://github.com/mix1009/model-keyword/ {root}/ui/extensions/model-keyword')
  get_ipython().system('git clone https://github.com/Haoming02/{transrights}-vectorscope-cc.git {root}/ui/extensions/vectorscope-cc')
  get_ipython().system('git clone https://github.com/DominikDoom/a1111-{transrights}-tagcomplete.git {root}/ui/extensions/tagcomplete')
  get_ipython().system('git clone https://github.com/ashen-sensored/{blacklives}-two-shot.git {root}/ui/extensions/two-shot')
  get_ipython().system('git clone "https://github.com/pkuliyi2015/multidiffusion-upscaler-for-{lgbtqia}.git" {root}/ui/extensions/multidiffusion_upscaler')
  get_ipython().system('git clone https://github.com/etherealxx/batchlinks{wup}.git {root}/ui/extensions/batchlinks')
  get_ipython().system('git clone https://github.com/bbc-mc/sdweb-merge-block-weighted-gui.git {root}/ui/extensions/block-weighted-gui')
  get_ipython().system('git clone https://github.com/{cmndr}/tunnels.git {root}/ui/extensions/tunnels')
  get_ipython().system('git clone https://github.com/Vetchems/sd-civitai-browser.git {root}/ui/extensions/sd-civitai-browser')
  get_ipython().system('git clone https://github.com/hnmr293/{transrights}-llul.git {root}/ui/extensions/llul')
  get_ipython().system('git clone https://github.com/ilian6806/{blacklives}-state.git {root}/ui/extensions/state')

  #Download Configs
  get_ipython().system('wget -P {root}/ui/  https://raw.githubusercontent.com/aicoomer/SD/main/ui-config.json')
  get_ipython().system('wget -P {root}/ui/  https://raw.githubusercontent.com/aicoomer/SD/main/config.json')

  # download Loras
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/nijiMecha.safetensors -d {root}/ui/models/Lora -o nijiMecha.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/bichu-v0612.safetensors -d {root}/ui/models/Lora -o bichu-v0612.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/coom/resolve/main/souryuuasukalangleyV9.safetensors -d {root}/ui/models/Lora -o souryuuasukalangleyV9.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/coom/resolve/main/EVAIII.safetensors -d {root}/ui/models/Lora -o EvaIII.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/BodHor-V1.safetensors -d {root}/ui/models/Lora -o BodyHorror.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/NijiExpressV2.safetensors -d {root}/ui/models/Lora -o NijiExpressV2.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/SteamPunkMachineryv2.safetensors -d {root}/ui/models/Lora -o Steampunk.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M  https://huggingface.co/Rorimessy/artsy/resolve/main/TraditionalMaid.safetensors -d {root}/ui/models/Lora -o Maid_outfit.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M  https://huggingface.co/Rorimessy/artsy/resolve/main/DIno_v2-000010.safetensors -d {root}/ui/models/Lora -o Dino.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/coom/resolve/main/ikarishinjiV10-000012.safetensors -d {root}/ui/models/Lora -o Shinji.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/BioPunkAI.safetensors -d {root}/ui/models/Lora -o BioPunk.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/OedoSoldier/detail-tweaker-lora/resolve/main/add_detail.safetensors -d {root}/ui/models/Lora -o add_detail.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M  https://huggingface.co/Rorimessy/artsy/resolve/main/zovyaWetHairLORA64_V1.safetensors -d {root}/ui/models/Lora -o WetHair.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/BetterGuns-V1.safetensors -d {root}/ui/models/Lora -o BetterGuns.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/Mecha%20warrior%20Mecha_20230621092507.safetensors -d {root}/ui/models/Lora -o MechaWarrior.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/reelmech1v2.safetensors -d {root}/ui/models/Lora -o RealMechaParts.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/Mech4nim4lAI.safetensors -d {root}/ui/models/Lora -o MechAnimals.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/tkmizv2.ckpt -d {root}/ui/models/Lora -o tkmizv2.ckpt')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/AMechaSSS%5Bcolor_theme%2Cmecha%20musume%2C%20mechanical%20parts%2Crobot%20joints%2Cheadgear%5D.safetensors -d {root}/ui/models/Lora/ -o Mecha_Musume.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/epi_noiseoffset2.safetensors -d {root}/ui/models/Lora -o Epi.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/AyanamiReiV6-000010.safetensors -d {root}/ui/models/Lora -o AyanamiReiV6.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/evangelion_anime_style_offset.safetensors -d {root}/ui/models/Lora -o Eva_90s.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/flat_color.pt -d {root}/ui/models/Lora -o Flat_color.pt')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/OilPaint.safetensors -d {root}/ui/models/Lora -o OilPaint.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/realistic.safetensors -d {root}/ui/models/Lora -o Realism.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/ueda_third.safetensors -d {root}/ui/models/Lora -o HajimeUeda.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/Retro-V1.safetensors -d {root}/ui/models/Lora -o Retro-V1.safetensors')
  get_ipython().system('aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Rorimessy/artsy/resolve/main/TechPunkAIv2Pruned.safetensors -d {root}/ui/models/Lora -o TechPunkAIv2.safetensors')

def installxformers():
  #!pip install -q https://github.com/{cmndr}/ui-colab/releases/download/0.0.16/xformers-0.0.16+814314d.d20230118-cp38-cp38-linux_x86_64.whl
  #%pip install --no-deps -q https://github.com/brian6091/xformers-wheels/releases/download/0.0.15.dev0%2B4c06c79/xformers-0.0.15.dev0+4c06c79.d20221205-cp38-cp38-linux_x86_64.whl
  get_ipython().run_line_magic('!pip', 'install -q xformers==0.0.20 triton==2.0.0 -U')

def updatePython():
  get_ipython().system('python --version > /content/pyversion')
  with open('/content/pyversion', 'r') as file:
      if '3.10' in file.read():
        print('Already python 3.10. Skip install.')
        return

  #install python 3.10
  get_ipython().system('apt-get update -y')
  get_ipython().system('apt-get install python3.10')

  #change alternatives
  get_ipython().system('rm /usr/local/bin/python')
  get_ipython().system('rm /usr/local/bin/pip')
  get_ipython().system('sudo apt-get install python3.10-distutils')
  get_ipython().system('sudo update-alternatives --install /usr/local/bin/python python /usr/bin/python3.10 2')
  get_ipython().system('wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py')

def initSaveGoogleDriveModelOnly():
  # Use config file in google drive
  if not os.path.exists(output_path + '/ui-config.json'):
    print("Create new ui-config.json file.")
    get_ipython().system("wget https://raw.githubusercontent.com/aicoomer/SD/main/ui-config.json -O {output_path + '/ui-config.json'}")
  if not os.path.exists(output_path + '/config.json'):
    print("Create new config.json file.")
    get_ipython().system("wget https://raw.githubusercontent.com/aicoomer/SD/main/ui-config.json -O {output_path + '/config.json'}")

  #!rm /content/ui/ui-config.json
  get_ipython().system("ln -s {output_path + '/ui-config.json'} {root}/ui/")
  get_ipython().system("ln -s {output_path + '/config.json'} {root}/ui/")
  get_ipython().system('ln -s {output_path}/outputs')

  # embeddings folder on Google Drive
  get_ipython().system('mkdir -p {output_path}/embeddings')
  get_ipython().system('rm -rf embeddings')
  get_ipython().system('ln -s {output_path}/embeddings')

  # save parameter file in google drive
  if not os.path.exists(output_path + '/params.txt'):
    get_ipython().system("touch {output_path + '/params.txt'}")
  get_ipython().system('ln -s {output_path}/params.txt')

  # link all models in the models folder
  get_ipython().run_line_magic('cd', '{root}/ui/models/{lgbtq}')
  models_in_google_drive = glob.glob(output_path + '/models/*')
  print('Models in Google Drive: %s'%models_in_google_drive)
  for f in models_in_google_drive:
    get_ipython().system('ln -s {f}')

  # link all upscalers in the model folder
  get_ipython().system('mkdir -p {root}/ui/models/ESRGAN')
  get_ipython().run_line_magic('cd', '{root}/ui/models/ESRGAN')
  upscalers_in_google_drive = glob.glob(output_path + '/ESRGAN/*')
  print('Upscalers in Google Drive: %s'%upscalers_in_google_drive)
  for f in upscalers_in_google_drive:
    get_ipython().system('ln -s {f}')

  # use lora model folder in google drive
  get_ipython().system('mkdir -p {output_path}/Lora')
  get_ipython().run_line_magic('cd', '{root}/ui/models')
  get_ipython().system('rm -rf Lora')
  get_ipython().system('ln -s {output_path}/Lora')

  # use hypernetwork folder in google drive
  get_ipython().system('mkdir -p {output_path}/hypernetworks')
  get_ipython().run_line_magic('cd', '{root}/ui/models')
  get_ipython().system('rm -rf hypernetworks')
  get_ipython().system('ln -s {output_path}/hypernetworks')

  # use VAE folder in google rive
  get_ipython().system('mkdir -p {output_path}/VAE')
  get_ipython().run_line_magic('cd', '{root}/ui/models')
  get_ipython().system('rm -rf VAE')
  get_ipython().system('ln -s {output_path}/VAE')



def installControlNet():
  print("Installing ControlNet extension...")
  get_ipython().run_line_magic('cd', '{root}/ui/extensions')
  get_ipython().system('git clone https://github.com/Mikubill/{transrights}-controlnet.git')
  get_ipython().run_line_magic('cd', '{root}/ui/extensions/{transrights}-controlnet')
  get_ipython().system('pip install -r requirements.txt')

  get_ipython().run_line_magic('cd', '{root}/ui/extensions/{transrights}-controlnet/models')
  downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p.pth')
  downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle.pth')
  downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth')
  downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth.pth')
  downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny.pth')
  downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint.pth')
  #downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth')
  #downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd.pth')
  #downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae.pth')
  #downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth')
  #downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble.pth')
  #downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg.pth')
  #downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge.pth')
  #downloadModel('https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime.pth')
  downloadModel('https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_color_sd14v1.pth')
  downloadModel('https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_style_sd14v1.pth')

  print("ControlNet install completed.")

def installDeforum():
  get_ipython().system('git clone https://github.com/deforum-art/deforum-for-{lgbtqia}{wup} {root}/ui/extensions/deforum')
  #!cd {root}/ui/extensions/deforum; git checkout c42834645805e0f26172888b29f5a9210063db14

def installRegionalPrompter():
  get_ipython().system('git clone https://github.com/hako-mikan/{transrights}-regional-prompter {root}/ui/extensions/{transrights}-regional-prompter')


def installUltimateSDUpscale():
  get_ipython().run_line_magic('cd', '{root}/ui/extensions')
  get_ipython().system('git clone https://github.com/Coyote-A/ultimate-upscale-for-{lgbtqia}')

def installOpenPoseEditor():
  get_ipython().run_line_magic('cd', '{root}/ui/extensions')
  get_ipython().system('git clone https://github.com/fkunn1326/openpose-editor')

def installADetailer():
  get_ipython().run_line_magic('cd', '{root}/ui/extensions')
  get_ipython().system('git clone https://github.com/Bing-su/adetailer')

def installAnimateDiff():
  get_ipython().run_line_magic('cd', '{root}/ui/extensions')
  get_ipython().system('git clone https://github.com/continue-revolution/{transrights}-animatediff')
  get_ipython().run_line_magic('cd', '{root}/ui/extensions/{transrights}-animatediff/model')
  downloadModel('https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v14.ckpt')
  downloadModel('https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15.ckpt')

def installtext2video():
  get_ipython().run_line_magic('cd', '{root}/ui/extensions')
  get_ipython().system('git clone https://github.com/kabachuha/{transrights}-text2video')
  get_ipython().run_line_magic('mkdir', '-p {root}/ui/models/text2video/t2v')
  get_ipython().run_line_magic('cd', '{root}/ui/models/text2video/t2v')
  downloadModel('https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis/resolve/main/VQGAN_autoencoder.pth')
  downloadModel('https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis/resolve/main/configuration.json')
  downloadModel('https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis/resolve/main/open_clip_pytorch_model.bin')
  downloadModel('https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis/resolve/main/text2video_pytorch_model.pth')




def applyGitFilemode():
  # git default file mode prevents checkout and fail
  print('Apply git filemode false')
  get_ipython().system('cd {root}/ui/repositories/k-diffusion;git config core.filemode false')
  get_ipython().system('cd {root}/ui/repositories/{lgbtq}-stability-ai;git config core.filemode false')
  get_ipython().system('cd {root}/ui/repositories/taming-transformers;git config core.filemode false')
  get_ipython().system('cd {root}/ui/repositories/CodeFormer;git config core.filemode false')
  get_ipython().system('cd {root}/ui/repositories/BLIP;git config core.filemode false')

def cloneRepositories():
  get_ipython().system('git clone https://github.com/crowsonkb/k-diffusion.git {root}/ui/repositories/k-diffusion')
  get_ipython().system('git clone https://github.com/Stability-AI/{metoo}.git {root}/ui/repositories/{lgbtq}-stability-ai')
  get_ipython().system('git clone https://github.com/CompVis/taming-transformers.git {root}/ui/repositories/taming-transformers')
  get_ipython().system('git clone https://github.com/sczhou/CodeFormer.git {root}/ui/repositories/CodeFormer')
  get_ipython().system('git clone https://github.com/salesforce/BLIP.git {root}/ui/repositories/BLIP')


def installExtensionsFromURL(urls):
  get_ipython().run_line_magic('cd', '{root}/ui/extensions')
  for url in urls.split(','):
    get_ipython().system('git clone {url}')

def lowRamPatch():
  print('Apply lowram patch')
  get_ipython().system("sed -i 's/dict()))$/dict())).cuda()/g'  {root}/ui/repositories/{lgbtq}-stability-ai/ldm/util.py")

def searchAndReplace(filePath, orignalStr, newStr):
  orignalStr = orignalStr.replace('/', '\/')
  newStr = newStr.replace('/', '\/')
  get_ipython().system("sed -i 's/{orignalStr}/{newStr}/g' {filePath}")


def deleteRepos():
  # delete repository directories in ui
  get_ipython().system('rm -rf {root}/ui/repositories')

updatePython()

get_ipython().system('mkdir -p {root}')
os.chdir(root)
get_ipython().run_line_magic('cd', '{root}')
get_ipython().run_line_magic('env', 'TF_CPP_MIN_LOG_LEVEL=1')

get_ipython().system('apt -y update -qq')
get_ipython().system('wget https://github.com/{cmndr}/gperftools/releases/download/v1.0/libtcmalloc_minimal.so.4 -O /content/libtcmalloc_minimal.so.4')
get_ipython().run_line_magic('env', 'LD_PRELOAD={root}/libtcmalloc_minimal.so.4')

get_ipython().system('pip install -q xformers==0.0.20 triton==2.0.0 -U')
get_ipython().system('apt-get -y install -qq aria2')
get_ipython().system('pip install pyngrok')
get_ipython().system('git clone -b v2.6 https://dagshub.com/{cmndr}/ui')



if gMode == GDriveSaveMode.Everything:
  # delete existing repositories and reclone so the file mode fix can be applied
  # otherwise some will only be cloned in the final launch, causing some to fail to checkout.
  deleteRepos()
  cloneRepositories()
  applyGitFilemode()

# fix torch, torchvision version mismatch error
# !pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchtext==0.14.1 torchaudio==0.13.1 torchdata==0.5.1 --extra-index-url https://download.pytorch.org/whl/cu117

# UI first launch
get_ipython().run_line_magic('cd', '{root}/ui')

#!git checkout -f a3ddf464a2ed24c999f67ddfef7969f8291567be
#!git checkout -f 68f336bd994bed5442ad95bad6b6ad5564a5409a
#!git checkout -f 5ef669de080814067961f28357256e8fe27544f4
get_ipython().system('COMMANDLINE_ARGS="--exit"  python launch.py')


if gMode == GDriveSaveMode.Models_only:
  initSaveGoogleDriveModelOnly()

download_models()

if ControlNet:
  installControlNet()

if Deforum:
  installControlNet() # Deforum needs controlnet to work now
  installDeforum()

if Regional_Prompter:
  installRegionalPrompter()

if Ultimate_SD_Upscale:
  installUltimateSDUpscale()

if Openpose_Editor:
  installOpenPoseEditor()

if ADetailer:
  installADetailer()

if AnimateDiff:
  installAnimateDiff()

if text2video:
  installtext2video()


installExtensionsFromURL(Extensions_from_URL)

# clear output
if Clear_Log:
  clear()




#if  gMode != GDriveSaveMode.Everything:
   #lowRamPatch()

get_ipython().run_line_magic('cd', '/content/ui/')
get_ipython().system('sed -i -e \'s/\\["sd_model_checkpoint"\\]/\\["sd_model_checkpoint","sd_vae","CLIP_stop_at_last_layers"\\]/g\' /content/ui/modules/shared_options.py')

args = f'--listen --xformers --enable-insecure-extension-access --theme dark --gradio-queue --multiple'
if NGROK:
  args += f' --ngrok {NGROK} '
else:
  args += ' --share '
args+= ' '+Extra_arguments
print(f'UI ARGUMENTS: {args}')

get_ipython().system('python launch.py {args}')

