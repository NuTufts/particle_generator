############################################################################
# argparser.py
# Author: Kai Stewart
# Organization: Tufts University
# Department: Physics
# Date: 10.08.2019
# Purpose: - This python script is designed to provide model-agnostic command
#            line argument parsing capabilities for PyTorch models associated
#            with the particle generator project.
#          - Functionality includes instantiation of argument parser objects
#            both for training and deploying PyTorch models.
############################################################################

# System Imports
from argparse import ArgumentParser

# Training argument parser function
def train_parser():
    '''
        Argument Parser Function for model training
        Does: prepares a command line argument parser object with
              functionality for training a generative model
        Args: None
        Returns: argument parser object
    '''
    usage = "Command line arguement parser for set up " + \
            "of PyTorch particle generator model training."
    parser = ArgumentParser(description=usage)

    # model: string that selects the type of model to be trained
    #        options: GAN, AE, EWM
    parser.add_argument('--model', type=str, default='',
                        help='String that selects the model - options: \
                            gan, ae, conv_ae, ewm, ewm_conv | (default: &(default)s)')
    # checkpoint: string path to saved model checkpoint. If used with
    #             train function, model will resume training from checkpoint
    #             If used with deploy function, model will used saved weights.
    parser.add_argument('--checkpoint', type=str, default='',
                        help='String path to saved model checkpoint. If used \
                            with training function, model will resume trainig \
                                from that checkpoint. If used with deploy \
                                    function, model will deploy with save weights. \
                                        | (default: &(default)s) ')
    ################## Data Loading ######################
    ######################################################
    # MNIST: For proof-of-concept purposes. Overrides other data loading
    #        options and uses the built-in torch MNIST dataset loading function
    parser.add_argument('--MNIST', type=bool, default=False,
                        help='Toggle to train model on MNIST dataset. Overrides \
                            other data loading options and uses the built-in \
                                torch MNIST dataset loading functionality | \
                                    (default: &(default)s)')
    # data_root: path to training data folder (top level)
    parser.add_argument('--data_root', type=str, default='',
                        help='Full path to training data folder \
                            | (default: &(default)s)')
    # save_root: path where training output is saved
    parser.add_argument('--save_root', type=str, default='/train_save',
                        help='Path where training output should be saved \
                            | (default: &(default)s)')
    # dataset: - which LArCV1 dataset to use (512, 256, 128, 64, 32)
    parser.add_argument('--dataset', type=int, default=256,
                        help='Which crop size of the LArCV1 dataset to use, or \
                            | (default: &(default)s)')
    parser.add_argument('--vec_root', type=str, default='',
                        help='Full path to test vectors data folder used to compute \
                             the early stopping criterion for the ewm model training \
                            | (default: &(default)s)')
    parser.add_argument('--ewm_root', type=str, default='',
                        help='Full path to set of trained EWM models \
                            | (default: &(default)s)')
    #########################################
    ## Torch DataLoader Key Word Arguments ##
    #########################################
    # batch_size: size of training data batches
    parser.add_argument('--batch_size', type=int, default=24,
                        help='Size of data batches to use during model training\
                             | (default: &(default)s')
    # num_epochs: number of epochs to train model(s)
    parser.add_argument('--num_epochs', type=int, default=1,
                        help='Number of epochs over which to train the model(s)\
                             | (default: &(default)s)')
    # sample_size: number of samples to generate during training
    parser.add_argument('--sample_size', type=int, default=8,
                        help='Number of image samples to be generated during\
                             training (progress check) | (default: &(default)s)')
    # gpu: which GPU to train the model(s) on
    parser.add_argument('--gpu', type=int, default=0,
                        help='Select gpu to use for training. If multi-gpu \
                            option is selected, then this option is ignored \
                                | (default: &(default)s)')
    # multi_gpu: toggle whether to train on multiple GPU's (if available)
    parser.add_argument('--multi_gpu', type=bool, default=False,
                        help='Select whether to use multiple GPUs to train \
                            model. This model overrides the --gpu flag \
                                | (default: &(default)s)')
    # shuffle: toggle shuffle on/off
    parser.add_argument('--shuffle', type=bool, default=True,
                        help='Toggle dataloader batch shuffle on/off \
                            | (default: &(default)s)')
    # drop_last: toggle drop last batch on/off if dataset
    #            size not divisible by batch size
    parser.add_argument('--drop_last', type=bool, default=False,
                        help='Toggle whether the dataloader should drop \
                            the last batch, if the dataset size is not \
                                divisible by the batch size \
                                    | (default: &(default)s)')
    # num_workers: number of worker threads for data io
    parser.add_argument('--num_workers', type=int, default=8,
                        help='Set number of worker threads for data io \
                            | (default: &(default)s)')

    ################# Model settings #####################
    ######################################################
    ## Linear GAN Model
    # n_hidden: number of hidden units in each network
    parser.add_argument('--n_hidden', type=int, default=512,
                        help='Number of hidden units in each layer of G and D \
                            | (default: &(default)s)')
    ### Generator Network
    # g_lr: generator learning rate
    parser.add_argument('--g_lr', type=float, default=1e-4,
                        help='Generator network learning rate \
                            | (default: &(default)s)')
    # g_opt: generator optimizer
    parser.add_argument('--g_opt', type=str, default='adam',
                        help='Generator network optimizer function - \
                            choices: adam, sgd | (default: &(default)s)')
    # z_dim: dimension of G input vector
    parser.add_argument('--z_dim', type=int, default=100,
                        help='Dimension of Generator network input vector \
                            size |(default: &(default)s)')

    ### Discriminator Network
    # d_lr: discriminator learning rate
    parser.add_argument('--d_lr', type=float, default=1e-4,
                        help='Discriminator network learning rate \
                            | (default: &(default)s)')
    # d_opt: discriminator optimizer
    parser.add_argument('--d_opt', type=str, default='adam',
                        help='Discriminator network optimizer function - \
                            choices: adam, sgd | (default: &(default)s)')

    ################# Shared Settings ####################
    ######################################################
    # beta: beta value (for Adam optimizer only)
    parser.add_argument('--beta', type=float, default=0.5,
                        help='Beta value for Adam optimizer \
                            | (default: &(default)s)')
    # momentum: momentum value (for SGD optimizer only)
    parser.add_argument('--p', type=float, default=0.9,
                        help='Momentum value for SGD optimizer \
                            | (default: &(default)s)')
    # n_layers: number of model layers
    parser.add_argument('--n_layers', type=int, default=4,
                        help='Number of desired model layers \
                            | (default: &(default)s)')
    # loss_fn: select the model's loss function -either
    #          MeanSquaredError or BinaryCrossEntropy
    parser.add_argument('--loss_fn', type=str, default='',
                        help="String specifiying which loss function \
                        the model should use | (default: &(default)s)")

    ######################################################
    ## AutoEncoder
    # l_dim: dimension of the encoders latent representation of the data
    parser.add_argument('--l_dim', type=int, default=20,
                        help='Dimension of the AE encoder latent space \
                            | (default: &(default)s)')
    # AE optimization function
    parser.add_argument('--ae_opt', type=str, default='adam',
                        help='Autoencoder optimization function - \
                            choices: adam, sgd | (default: &(default)s)')
    # AE learning rate
    parser.add_argument('--ae_lr', type=float, default=1e-4,
                        help='Autoencoder learning rate \
                            | (default: &(default)s)')
    parser.add_argument('--depth', type=int, default=32,
                        help='Depth of the feature maps in an instance of a \
                        Convolutional AutoEncoder -- must be divisible by 4 \
                        | (default: &(default)s)')

    ######################################################
    ## EWM Model
    # ewm_optim: optimizer function for EWM model training
    parser.add_argument('--psi_lr', type=float, default=1e-1,
                        help='Learning rate for EWM psi optimizer \
                            | (default: &(default)s)')
    ### Set memory size
    parser.add_argument('--mem_size', type=int, default=5000,
                        help='Size of memory arrays used in OTS computation \
                        | (default: %(default)s)')
    parser.add_argument('--ewm_target', type=str, default='',
                        help='Specify the model type from which the EWM targets \
                        were produced: conv or mlp | (default: %(default)s)')
    parser.add_argument('--tess_var', type=float, default=0.5,
                        help='Tessellation vector variance | (default: %(default)s)')

    return parser

# Deploy model argument parser function
def deploy_parser():
    '''
        Argument Parser Function for model training
        Does: prepares a command line argument parser object with
              functionality for deploying a trained generative model.
        Args: None
        Returns: argument parser object
    '''
    usage = "Command line arguement parser for deploying " + \
            "trained PyTorch particle generator models."
    parser = ArgumentParser(description=usage)

    # TODO: Write the parser arguments after deciding on a convention for how
    # model outputs, checkpoints, and experiments will be saved.

    return parser
