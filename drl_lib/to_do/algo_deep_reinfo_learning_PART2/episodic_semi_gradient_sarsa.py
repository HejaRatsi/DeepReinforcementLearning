import tqdm

import tensorflow as tf
import numpy as np

from drl_lib.to_do.world_PART2.contratDeepSingleAgentWithDiscreteActionsEnv import DeepSingleAgentWithDiscreteActionsEnv


def episodic_semi_gradient_sarsa(env: DeepSingleAgentWithDiscreteActionsEnv):
    pre_warm = 10
    epsilon = 0.1
    gamma = 0.9
    max_episodes_count = 100
    print_every_n_episodes = 10

    #INTIALIZE VALUE-FUNCTION WEIGHT (IN ALGO)
    state_description_length = env.state_description_length()
    max_actions_count = env.max_actions_count()

    q = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation=tf.keras.activations.tanh,
                              input_dim=(state_description_length + max_actions_count)),
        tf.keras.layers.Dense(1, activation=tf.keras.activations.linear),
    ])

    # q = tf.keras.Sequential([
    #     tf.keras.layers.Dense(16, activation=tf.keras.activations.tanh,
    #                           input_dim=state_description_length),
    #     tf.keras.layers.Dense(max_actions_count, activation=tf.keras.activations.linear),
    # ])

    q.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.mse)


    #LOOP FOR EACH EPISODE (IN ALGO)
    for episode_id in tqdm.tqdm(range(max_episodes_count)):
        #S,A <- INITIAL STATE AND ACTION OF EPISODE (IN ALGO)
        env.reset()

        #LOOP FOR EACH STEP OF EPISODE
        while not env.is_game_over():
            #S <- S_p (IN ALGO) (mais à la fin dans l'algo)
            #A <- A_p (IN ALGO) (mais à la fin dans l'algo)
            s = env.state_description()
            available_actions = env.available_actions_ids()

            # TAKE ACTION A, OBSERVE R,S_p (IN ALGO)
            chosen_action = None
            chosen_action_q_value = None
            if episode_id < pre_warm or np.random.uniform(0.0, 1.0) < epsilon:
                chosen_action = np.random.choice(available_actions)
            else:
                chosen_action = None
                chosen_action_q_value = None
                all_q_inputs = np.zeros((len(available_actions), state_description_length + max_actions_count))
                for i, a in enumerate(available_actions):
                    all_q_inputs[i] = np.hstack([s, tf.keras.utils.to_categorical(a, max_actions_count)])
                """
                HSTACK
                a = np.array((1,2,3))
                b = np.array((4,5,6))
                np.hstack((a,b))
                -->> array([1, 2, 3, 4, 5, 6])
                
                SQUEEZE
                x = np.array([[[0], [1], [2]]])
                y = np.array([[0], [1], [2]])
                
                print(np.squeeze(x))
                -->> [ 0  1  2  6 ]
                print(np.squeeze(y))
                -->> [ 0  1  2  6 ]
                """
                all_q_values = np.squeeze(q.predict(all_q_inputs))
                chosen_action = available_actions[np.argmax(all_q_values)]
                chosen_action_q_value = np.max(all_q_values)
                # q_value = q.predict(np.array([q_inputs]))[0][0]
                # if chosen_action is None or chosen_action_q_value < q_value:
                #     chosen_action = a
                #     chosen_action_q_value = q_value


            if episode_id % print_every_n_episodes == 0:
                print(f'State Description : {s}')
                print(f'Chosen action : {chosen_action}')
                print(f'Chosen action value : {chosen_action_q_value}')

            previous_score = env.score()
            env.act_with_action_id(chosen_action)
            r = env.score() - previous_score
            s_p = env.state_description()

            #IF S_p IS TERMINAL (IN ALGO)
            if env.is_game_over():
                target = r
                q_inputs = np.hstack([s, tf.keras.utils.to_categorical(chosen_action, max_actions_count)])
                q.train_on_batch(np.array([q_inputs]), np.array([target]))
                #GO TO NEXT EPISODE (IN ALGO)
                break

            next_available_actions = env.available_actions_ids()

            #CHOOSE A_p AS A FUNCTION (IN ALGO)
            if episode_id < pre_warm or np.random.uniform(0.0, 1.0) < epsilon:
                next_chosen_action = np.random.choice(next_available_actions)
            else:
                next_chosen_action = None
                next_chosen_action_q_value = None
                for a in next_available_actions:
                    q_inputs = np.hstack([s_p, tf.keras.utils.to_categorical(a, max_actions_count)])
                    q_value = q.predict(np.array([q_inputs]))[0][0]
                    if next_chosen_action is None or next_chosen_action_q_value < q_value:
                        next_chosen_action = a
                        next_chosen_action_q_value = q_value


            # W <- W + alpha ... (IN ALGO)
            next_q_inputs = np.hstack([s_p, tf.keras.utils.to_categorical(next_chosen_action, max_actions_count)])
            next_chosen_action_q_value = q.predict(np.array([next_q_inputs]))[0][0]

            target = r + gamma * next_chosen_action_q_value

            q_inputs = np.hstack([s, tf.keras.utils.to_categorical(chosen_action, max_actions_count)])
            q.train_on_batch(np.array([q_inputs]), np.array([target]))

