from pathlib import Path


class Params:
    random_state = 42
    assets_path = Path('./assets')
    original = assets_path / 'orignal' / 'data.csv'
    data = assets_path / 'dzongkha_data'
    features = assets_path / 'dzongkha_features'
    models = assets_path / 'dzongkha_models'
    metrics = assets_path / 'metrics'
