import datetime

def get_influence_time(data, date, fish, target_feature_name):
    observe_dates = [date + datetime.timedelta(days=day) for day in range(4)]
    filtred_data = {observe_date: [(eval(_.features), _.temperature, _.time) for _ in data if
                                   _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
    influence = []
    for index, observe_date in enumerate(observe_dates):
        explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
        for features, temperature, time in explain_prediction:
            for feature, value, weight in features:
                feature_name, day_shift, time_shift = feature
                if 0 <= index * 24 + time - (day_shift * 24 + time_shift) < 24 and feature_name == target_feature_name:
                    influence.append((index, time, weight, value))
    influence = sorted(influence)
    return [(_[0], _[1]) for _ in influence]


def get_influence_days(data, date, fish, target_feature_name):
    observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
    filtred_data = {observe_date: [(eval(_.features), _.temperature, _.time) for _ in data if
                                   _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
    influence = []
    for index, observe_date in enumerate(observe_dates):
        explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
        for features, temperature, time in explain_prediction:
            for feature, value, weight in features:
                feature_name, day_shift, time_shift = feature
                if 0 <= index * 24 + time - (day_shift * 24 + time_shift) < 24 and feature_name == target_feature_name:
                    influence.append((observe_date, time, weight, value))
    return list(set([_[0] for _ in influence]))


def get_influence_time_prob(data, date, fish, lower_bound, upper_bound):
    observe_dates = [date + datetime.timedelta(days=day) for day in range(4)]

    filtred_data = {observe_date: [(_.prob, _.time) for _ in data if
                                   _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
    influence_low = []
    influence_up = []
    for index, observe_date in enumerate(observe_dates):
        explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
        for prob, time in explain_prediction:
            if prob < lower_bound:
                influence_low.append((index, time))
            if prob > upper_bound:
                influence_up.append((index, time))
    influence_low = sorted(influence_low)
    influence_up = sorted(influence_up)
    return influence_low, influence_up


def get_influence_days_prob(data, date, fish, lower_bound, upper_bound):
    observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
    filtred_data = {observe_date: [(_.prob, _.time) for _ in data if
                                   _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
    influence_low = []
    influence_up = []
    for index, observe_date in enumerate(observe_dates):
        explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
        for prob, time in explain_prediction:
            if prob < lower_bound:
                influence_low.append((observe_date))
            if prob > upper_bound:
                influence_up.append((observe_date))
    influence_low = sorted(influence_low)
    influence_up = sorted(influence_up)
    return list(set(influence_low)), list(set(influence_up))
