from sklearn.ensemble import RandomForestClassifier


def train_model(x_train, y_train, n_estimators=100):
    """Train a random forest classifier."""
    model = RandomForestClassifier(n_estimators=n_estimators)
    model.fit(x_train, y_train)
    return model
