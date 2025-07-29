

# <font color="LighBlue">Stable Audio Open</font>

## 指标

|                         FD Openl3 ↓                          |                          KL PasST ↓                          |                     CLAP Score ↑                      |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :---------------------------------------------------: |
| ![sa_FD_Openl3_withmean](./assets/sa_FD_Openl3_withmean.png) | <img src="./assets/sa_KL_PasST_withmean.png" alt="kld_plot"  /> | ![sa_CLAP_Score](./assets/sa_CLAP_Score_withmean.png) |
|                  [0, 3, 18, 20, 21, 22, 23]                  |             [0, 2, 3, 4, 11, 12, 13, 18, 20, 23]             |           [2, 3, 4, 5, 12, 13, 16, 22, 23]            |



- ### FD Openl3 ↓

![sa_FD_Openl3_withmean](./assets/sa_FD_Openl3_withmean.png)

- ###  KL PasST ↓

  <img src="./assets/sa_KL_PasST_withmean.png" alt="kld_plot"  />

- ### CLAP Score ↑

![sa_CLAP_Score_withmean](./assets/sa_CLAP_Score_withmean.png)





# Music Editing Examples

|            Text Prompt             | Original Audio |
| :--------------------------------: | :------------: |
| Format: Solo \| Instruments: Piano |                |

|    Edit Method     |                Edit Prompt                | Edit Audio |
| :----------------: | :---------------------------------------: | :--------: |
| VITAL_LAYERS = [3] |    Format: Solo \|Instruments: Guitar     |            |
| VITAL_LAYERS = [3] | Format: Solo \|Instruments: Piano, Guitar |            |
|                    |                                           |            |
|                    |                                           |            |
|                    |                                           |            |
|                    |                                           |            |
|                    |                                           |            |



|                    Text Prompt                    | Original Audio |
| :-----------------------------------------------: | :------------: |
| Instruments: synthesizer arpeggio<br />合成器琶音 |                |

|    Edit Method     |                Edit Prompt                | Edit Audio |
| :----------------: | :---------------------------------------: | :--------: |
| VITAL_LAYERS = [3] |            Instruments: Guitar            |            |
| VITAL_LAYERS = [3] | Instruments: synthesizer arpeggio, Guitar |            |
|                    |                                           |            |
|                    |                                           |            |
|                    |                                           |            |
|                    |                                           |            |
|                    |                                           |            |



|                         Text Prompt                          | Original Audio |
| :----------------------------------------------------------: | :------------: |
| A lush Pop instrumental featuring 808 drum machines, big synthesizer pads and catchy melodies. The mood is cool, modern and fun. 115 BPM<br />一款华丽的流行乐器，有808鼓机、大合成器垫和朗朗上口的旋律。气氛凉爽、现代、有趣。115 BPM |                |

|    Edit Method     |                         Edit Prompt                          | Edit Audio |
| :----------------: | :----------------------------------------------------------: | :--------: |
| VITAL_LAYERS = [3] | A lush Pop instrumental featuring guitar and catchy melodies. The mood is cool, modern and fun. 115 BPM |            |
| VITAL_LAYERS = [3] | A lush Pop instrumental featuring guitar, 808 <br/>drum machines, big synthesizer pads and catchy melodies. The mood is cool, modern and fun. 115 BPM |            |
|                    |                                                              |            |
|                    |                                                              |            |
|                    |                                                              |            |
|                    |                                                              |            |
|                    |                                                              |            |





