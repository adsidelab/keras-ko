
from guides_master import GUIDES_MASTER
from models_master import MODELS_MASTER
from layers_master import LAYERS_MASTER
from callbacks_master import CALLBACKS_MASTER
from utils_master import UTILS_MASTER
from examples_master import EXAMPLES_MASTER


MASTER = {
    'path': '/',
    'title': '케라스: 파이썬 딥러닝 라이브러리',
    'children': [
        {
            'path': 'about',
            'title': '케라스에 대하여'  # TODO
        },
        {
            'path': 'getting_started/',
            'title': '시작하기',
            'children': [
                {
                    'path': 'intro_to_keras_for_engineers',
                    'title': '엔지니어에게 맞는 케라스 소개',
                },
                {
                    'path': 'intro_to_keras_for_researchers',
                    'title': '연구자에게 맞는 케라스 소개',
                },
                {
                    'path': 'ecosystem',
                    'title': '케라스 생태계',
                },
                {
                    'path': 'learning_resources',
                    'title': '학습 자료',
                },
                {
                    'path': 'faq',
                    'title': '자주 묻는 질문',
                    'outline': False,
                },
            ]
        },
        GUIDES_MASTER,
        {
            'path': 'api/',
            'title': '케라스 API',
            'toc': True,
            'children': [
                MODELS_MASTER,
                LAYERS_MASTER,
                CALLBACKS_MASTER,
                {
                    'path': 'preprocessing/',
                    'title': '데이터 전처리',
                    'toc': True,
                    'children': [
                        {
                            'path': 'image',
                            'title': '이미지 데이터 전처리',
                            'generate': [
                                'tensorflow.keras.preprocessing.image_dataset_from_directory',
                                'tensorflow.keras.preprocessing.image.load_img',
                                'tensorflow.keras.preprocessing.image.img_to_array',
                                'tensorflow.keras.preprocessing.image.ImageDataGenerator',  # LEGACY
                                'tensorflow.keras.preprocessing.image.ImageDataGenerator.flow',  # LEGACY
                                'tensorflow.keras.preprocessing.image.ImageDataGenerator.flow_from_dataframe',  # LEGACY
                                'tensorflow.keras.preprocessing.image.ImageDataGenerator.flow_from_directory',  # LEGACY
                            ],
                        },
                        {
                            'path': 'timeseries',
                            'title': '시계열 데이터 전처리',
                            'generate': [
                                'tensorflow.keras.preprocessing.timeseries_dataset_from_array',
                                'tensorflow.keras.preprocessing.sequence.pad_sequences',
                                'tensorflow.keras.preprocessing.sequence.TimeseriesGenerator',  # LEGACY
                            ]
                        },
                        {
                            'path': 'text',
                            'title': '텍스트 데이터 전처리',
                            'generate': [
                                'tensorflow.keras.preprocessing.text_dataset_from_directory',
                                'tensorflow.keras.preprocessing.text.Tokenizer',  # LEGACY
                            ]
                        },
                    ]
                },
                {
                    'path': 'optimizers/',
                    'title': '옵티마이저',
                    'toc': True,
                    'generate': [
                        'tensorflow.keras.optimizers.Optimizer.apply_gradients',
                        'tensorflow.keras.optimizers.Optimizer.weights',
                        'tensorflow.keras.optimizers.Optimizer.get_weights',
                        'tensorflow.keras.optimizers.Optimizer.set_weights',
                    ],
                    'children': [
                        {
                            'path': 'sgd',
                            'title': 'SGD',
                            'generate': ['tensorflow.keras.optimizers.SGD']
                        },
                        {
                            'path': 'rmsprop',
                            'title': 'RMSprop',
                            'generate': ['tensorflow.keras.optimizers.RMSprop']
                        },
                        {
                            'path': 'adam',
                            'title': 'Adam',
                            'generate': ['tensorflow.keras.optimizers.Adam']
                        },
                        {
                            'path': 'adadelta',
                            'title': 'Adadelta',
                            'generate': ['tensorflow.keras.optimizers.Adadelta']
                        },
                        {
                            'path': 'adagrad',
                            'title': 'Adagrad',
                            'generate': ['tensorflow.keras.optimizers.Adagrad']
                        },
                        {
                            'path': 'adamax',
                            'title': 'Adamax',
                            'generate': ['tensorflow.keras.optimizers.Adamax']
                        },
                        {
                            'path': 'Nadam',
                            'title': 'Nadam',
                            'generate': ['tensorflow.keras.optimizers.Nadam']
                        },
                        {
                            'path': 'ftrl',
                            'title': 'Ftrl',
                            'generate': ['tensorflow.keras.optimizers.Ftrl']
                        },
                        {
                            'path': 'learning_rate_schedules/',
                            'title': '학습률 스케줄 API',
                            'toc': True,
                            'skip_from_toc': True,
                            'children': [
                                {
                                    'path': 'exponential_decay',
                                    'title': 'ExponentialDecay',
                                    'generate': ['tensorflow.keras.optimizers.schedules.ExponentialDecay']
                                },
                                {
                                    'path': 'piecewise_constant_decay',
                                    'title': 'PiecewiseConstantDecay',
                                    'generate': ['tensorflow.keras.optimizers.schedules.PiecewiseConstantDecay']
                                },
                                {
                                    'path': 'polynomial_decay',
                                    'title': 'PolynomialDecay',
                                    'generate': ['tensorflow.keras.optimizers.schedules.PolynomialDecay']
                                },
                                {
                                    'path': 'inverse_time_decay',
                                    'title': 'InverseTimeDecay',
                                    'generate': ['tensorflow.keras.optimizers.schedules.InverseTimeDecay']
                                },
                            ]
                        },
                    ]
                },
                {
                    'path': 'metrics/',
                    'title': '측정 지표',
                    'toc': True,
                    'children': [
                        {
                            'path': 'accuracy_metrics',
                            'title': '정확도',
                            'generate': [
                                'tensorflow.keras.metrics.Accuracy',
                                'tensorflow.keras.metrics.BinaryAccuracy',
                                'tensorflow.keras.metrics.CategoricalAccuracy',
                                'tensorflow.keras.metrics.TopKCategoricalAccuracy',
                                'tensorflow.keras.metrics.SparseTopKCategoricalAccuracy',
                            ],
                        },
                        {
                            'path': 'probabilistic_metrics',
                            'title': '확률 지표',  # TODO: easter egg for poisson
                            'generate': [
                                'tensorflow.keras.metrics.BinaryCrossentropy',
                                'tensorflow.keras.metrics.CategoricalCrossentropy',
                                'tensorflow.keras.metrics.SparseCategoricalCrossentropy',
                                'tensorflow.keras.metrics.KLDivergence',
                                'tensorflow.keras.metrics.Poisson',
                            ]
                        },
                        {
                            'path': 'regression_metrics',
                            'title': '회귀 지표',
                            'generate': [
                                'tensorflow.keras.metrics.MeanSquaredError',
                                'tensorflow.keras.metrics.RootMeanSquaredError',
                                'tensorflow.keras.metrics.MeanAbsoluteError',
                                'tensorflow.keras.metrics.MeanAbsolutePercentageError',
                                'tensorflow.keras.metrics.MeanSquaredLogarithmicError',
                                'tensorflow.keras.metrics.CosineSimilarity',
                                'tensorflow.keras.metrics.LogCoshError',
                            ]
                        },
                        {
                            'path': 'classification_metrics',
                            'title': 'True/False(양성/음성) 기반의 분류 지표',
                            'generate': [
                                'tensorflow.keras.metrics.AUC',
                                'tensorflow.keras.metrics.Precision',
                                'tensorflow.keras.metrics.Recall',
                                'tensorflow.keras.metrics.TruePositives',
                                'tensorflow.keras.metrics.TrueNegatives',
                                'tensorflow.keras.metrics.FalsePositives',
                                'tensorflow.keras.metrics.FalseNegatives',
                                'tensorflow.keras.metrics.PrecisionAtRecall',
                                'tensorflow.keras.metrics.SensitivityAtSpecificity',
                                'tensorflow.keras.metrics.SpecificityAtSensitivity',
                            ]
                        },
                        {
                            'path': 'segmentation_metrics',
                            'title': '이미지 분할 지표',
                            'generate': ['tensorflow.keras.metrics.MeanIoU']
                        },
                        {
                            'path': 'hinge_metrics',
                            'title': '"최대-마진" 분류를 위한 힌지 지표',
                            'generate': [
                                'tensorflow.keras.metrics.Hinge',
                                'tensorflow.keras.metrics.SquaredHinge',
                                'tensorflow.keras.metrics.CategoricalHinge',
                            ]
                        }
                    ]
                },
                {
                    'path': 'losses/',
                    'title': 'Losses',
                    'toc': True,
                    'children': [
                        {
                            'path': 'probabilistic_losses',
                            'title': '확률 손실',
                            'generate': [
                                'tensorflow.keras.losses.BinaryCrossentropy',
                                'tensorflow.keras.losses.CategoricalCrossentropy',
                                'tensorflow.keras.losses.SparseCategoricalCrossentropy',
                                'tensorflow.keras.losses.Poisson',

                                'tensorflow.keras.losses.binary_crossentropy',
                                'tensorflow.keras.losses.categorical_crossentropy',
                                'tensorflow.keras.losses.sparse_categorical_crossentropy',
                                'tensorflow.keras.losses.poisson',
                                'tensorflow.keras.losses.KLDivergence',
                                'tensorflow.keras.losses.kl_divergence',
                            ]
                        },
                        {
                            'path': 'regression_losses',
                            'title': '회귀 손실',
                            'generate': [
                                'tensorflow.keras.losses.MeanSquaredError',
                                'tensorflow.keras.losses.MeanAbsoluteError',
                                'tensorflow.keras.losses.MeanAbsolutePercentageError',
                                'tensorflow.keras.losses.MeanSquaredLogarithmicError',
                                'tensorflow.keras.losses.CosineSimilarity',

                                'tensorflow.keras.losses.mean_squared_error',
                                'tensorflow.keras.losses.mean_absolute_error',
                                'tensorflow.keras.losses.mean_absolute_percentage_error',
                                'tensorflow.keras.losses.mean_squared_logarithmic_error',
                                'tensorflow.keras.losses.cosine_similarity',
                                'tensorflow.keras.losses.Huber',
                                'tensorflow.keras.losses.huber',
                                'tensorflow.keras.losses.LogCosh',
                                'tensorflow.keras.losses.log_cosh',
                            ]
                        },
                        {
                            'path': 'hinge_losses',
                            'title': '"최대-마진" 분류를 위한 힌지 손실',
                            'generate': [
                                'tensorflow.keras.losses.Hinge',
                                'tensorflow.keras.losses.SquaredHinge',
                                'tensorflow.keras.losses.CategoricalHinge',

                                'tensorflow.keras.losses.hinge',
                                'tensorflow.keras.losses.squared_hinge',
                                'tensorflow.keras.losses.categorical_hinge',
                            ]
                        },
                    ],
                },
                {
                    'path': 'datasets/',
                    'title': '내장 데이터셋',
                    'toc': True,
                    'children': [
                        {
                            'path': 'mnist',
                            'title': 'MNIST 숫자 분류 데이터셋',
                            'generate': ['tensorflow.keras.datasets.mnist.load_data']
                        },
                        {
                            'path': 'cifar10',
                            'title': 'CIFAR10 이미지 분류 데이터셋',
                            'generate': ['tensorflow.keras.datasets.cifar10.load_data']
                        },
                        {
                            'path': 'cifar100',
                            'title': 'CIFAR100 이미지 분류 데이터셋',
                            'generate': ['tensorflow.keras.datasets.cifar100.load_data']
                        },
                        {
                            'path': 'imdb',
                            'title': 'IMDB 영화 리뷰 감성 분류 데이터셋',
                            'generate': [
                                'tensorflow.keras.datasets.imdb.load_data',
                                'tensorflow.keras.datasets.imdb.get_word_index',
                            ]
                        },
                        {
                            'path': 'reuters',
                            'title': '로이터 뉴스 분류 데이터셋',
                            'generate': [
                                'tensorflow.keras.datasets.reuters.load_data',
                                'tensorflow.keras.datasets.reuters.get_word_index',
                            ]
                        },
                        {
                            'path': 'fashion_mnist',
                            'title': '패션 MNIST 데이터셋',
                            'generate': ['tensorflow.keras.datasets.fashion_mnist.load_data']
                        },
                        {
                            'path': 'boston_housing',
                            'title': '보스턴 주택 가격 회귀 데이터셋',
                            'generate': ['tensorflow.keras.datasets.boston_housing.load_data']
                        },
                    ]
                },
                {
                    'path': 'applications/',
                    'title': '케라스 애플리케이션',
                    'children': [
                        {
                            'path': 'xception',
                            'title': 'Xception',
                            'generate': ['tensorflow.keras.applications.Xception'],
                        },
                        {
                            'path': 'efficientnet',
                            'title': 'EfficientNet B0~B7',
                            'generate': [
                                'tensorflow.keras.applications.EfficientNetB0',
                                'tensorflow.keras.applications.EfficientNetB1',
                                'tensorflow.keras.applications.EfficientNetB2',
                                'tensorflow.keras.applications.EfficientNetB3',
                                'tensorflow.keras.applications.EfficientNetB4',
                                'tensorflow.keras.applications.EfficientNetB5',
                                'tensorflow.keras.applications.EfficientNetB6',
                                'tensorflow.keras.applications.EfficientNetB7',
                            ],
                        },
                        {
                            'path': 'vgg',
                            'title': 'VGG16와 VGG19',
                            'generate': [
                                'tensorflow.keras.applications.VGG16',
                                'tensorflow.keras.applications.VGG19'
                            ],
                        },
                        {
                            'path': 'resnet',
                            'title': 'ResNet와 ResNetV2',
                            'generate': [
                                'tensorflow.keras.applications.ResNet50',
                                'tensorflow.keras.applications.ResNet101',
                                'tensorflow.keras.applications.ResNet152',
                                'tensorflow.keras.applications.ResNet50V2',
                                'tensorflow.keras.applications.ResNet101V2',
                                'tensorflow.keras.applications.ResNet152V2',
                            ],
                        },
                        {
                            'path': 'mobilenet',
                            'title': 'MobileNet와 MobileNetV2',
                            'generate': [
                                'tensorflow.keras.applications.MobileNet',
                                'tensorflow.keras.applications.MobileNetV2',
                            ]
                        },
                        {
                            'path': 'densenet',
                            'title': 'DenseNet',
                            'generate': [
                                'tensorflow.keras.applications.DenseNet121',
                                'tensorflow.keras.applications.DenseNet169',
                                'tensorflow.keras.applications.DenseNet201',
                            ]
                        },
                        {
                            'path': 'nasnet',
                            'title': 'NasNetLarge와 NasNetMobile',
                            'generate': [
                                'tensorflow.keras.applications.NASNetLarge',
                                'tensorflow.keras.applications.NASNetMobile',
                            ]
                        },
                        {
                            'path': 'inceptionv3',
                            'title': 'InceptionV3',
                            'generate': [
                                'tensorflow.keras.applications.InceptionV3',
                            ]
                        },
                        {
                            'path': 'inceptionresnetv2',
                            'title': 'InceptionResNetV2',
                            'generate': [
                                'tensorflow.keras.applications.InceptionResNetV2',
                            ]
                        },
                    ]
                },
                UTILS_MASTER,
            ]
        },
        EXAMPLES_MASTER,  # The examples section master will be mostly autogenerated.
        {
            'path': 'why_keras',
            'title': '왜 케라스인가?',
        },
        {
            'path': 'governance',
            'title': '커뮤니티 & 거버넌스',
        },
        {
            'path': 'contributing',
            'title': '케라스에 기여하기',
        },
        {
            'path': 'keras_tuner/',
            'title': 'KerasTuner',
        },
    ]
}
