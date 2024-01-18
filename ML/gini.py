import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")
print(data)


def G(df: pd.DataFrame, target):
    counts = df[target].value_counts()
    gini = 1 - ((counts / counts.sum()) ** 2).sum()
    return gini


def cart_tree(df: pd.DataFrame, target):
    features = df.drop([target], axis=1).columns
    values = {x: df[x].unique() for x in df}

    Gini = {}

    min_feature = features[0]
    min_ai = 10

    for feature in features:
        gi = pd.Series({v: G(df[df[feature] == v], target) for v in values[feature]})

        counts = [len(df[df[feature] == v]) for v in gi.index]
        ai = (gi * counts / len(df)).sum()

        Gini[feature] = gi

        if ai < min_ai:
            min_feature = feature
            min_ai = ai

    min_g = Gini[min_feature]
    return {
        min_feature: {
            v: (
                df[df[min_feature] == v][target].value_counts().to_dict()
                if min_g[v] == 0
                else cart_tree(
                    df[df[min_feature] == v].drop(columns=[min_feature]), target
                )
            )
            for v in min_g.index
        }
    }


def print_tree(tree, features, depth):
    for k in tree:
        if type(tree[k]) == dict:
            if k in features:
                print("\t" * depth, f"[{k}]:", end=" ")
            else:
                print("\t" * depth, k, ":", end=" ")
            tkk = list(tree[k].keys())
            if len(tkk) > 1 or tkk[0] in features:
                print()
            print_tree(tree[k], features, depth + 1)
        else:
            print(k)


def CART(df: pd.DataFrame, target):
    Tree = cart_tree(df, target)
    print_tree(Tree, df.drop(columns=[target]).columns, 0)


CART(data, "House")

# tennis = pd.read_csv("./Tennis.csv")
# CART(tennis, "Play")
