# Robertazzi_code_InternationalJournalNeuralSystems_2025
This repository contains the code associated with the article:

"Dynamic regulation of the serotonin-dopamine interaction within a meta-reinforcement learning framework encompassing the prefrontal cortex and basal ganglia", authored by F. Robertazzi, M. Vissani, E. Falotico, and published in the International Journal of Neural Systems.

## Installation
The code was tested with Python 3.8

Clone the repository:

```bash
git clone https://github.com/FedericaRobertazzi/Robertazzi_code_InternationalJournalNeuralSystems_2025.git
```
Requirements
+ Numpy 1.18.5
+ Pandas 1.0.5
+ Scipy 1.5.0
+ Matplotlib 3.2.2

## Folder Structure

The repository is composed of two different folders: 

Domapinergic_pathways_MetaLearning_StopSignalP: 

+ main_StopSignal_Paradigm_dopaminergic_pathways.py
+ neurons.py
+ synapses.py
+ action_probability.py
+ parameters_meta_learning.py
+ utility.py
+ mechanisms_meta_learning.py
+ parameters_and_metrics_computation.py
+ Appendix_A
  + params_D1.py
  + params_D2.py
  + results_concentration_response_curves_and_interaction.py
  + results_concentration_response_heatmaps.py
  + plots_example_part_A.py

Serotonin_Dopamine_closed_loop_MetaLearning_StopSignalP:

+ main_StopSignal_Paradigm_sero_dopa_closed_loop.py
+ neurons.py
+ synapses.py
+ neurotransmitters.py
+ action_probability.py
+ parameters_meta_learning.py
+ utility.py
+ mechanisms_meta_learning.py
+ parameters_and_metrics_computation.py
+ Appendix_B
  + results_StopSignal_Paradigm_closed_loop.py
  + results_inh_performance_open_and_closed_loop_comparison.py
  + results_closed_loop_accuracy_gain_coupling_config.py
  + results_entropy.py
  + reg_existence_params.py
  + plots_example_part_B.py

## Execution 

```bash
main_StopSignal_Paradigm_dopaminergic_pathways.py
main_StopSignal_Paradigm_sero_dopa_closed_loop.py
```

## License 
This project is licensed under the MIT License.

## Contact
In case of questions, contact: federica.robertazzi@santannapisa.it
