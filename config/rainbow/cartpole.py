### Rainbow DQN CratPole Config ###

env = {
    "name":"cartpole",
    "mode":"discrete",
    "render":False,
}

agent = {
    "name": "rainbow",
    "network": "rainbow",
    "optimizer": "adam",
    "learning_rate": 0.0000625,
    "gamma": 0.99,
    "explore_step": 20000,
    "buffer_size": 50000,
    "batch_size": 64,
    "start_train_step": 2000,
    "target_update_period": 1000,
    
    # MultiStep
    "n_step": 3,
    # PER
    "alpha": 0.6,
    "beta": 0.4,
    "learn_period": 4,
    "uniform_sample_prob": 1e-3,
    # C51
    "v_min": -10,
    "v_max": 10,
    "num_support": 51
}

train = {
    "training" : True,
    "load_path" : None,
    "run_step" : 100000,
    "print_period" : 1000,
    "save_period" : 10000,
    "test_iteration": 10,
    # distributed setting
    "update_period" : 8,
    "num_worker" : 8,
}