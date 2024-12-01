import matchers

class QueryBuilder:
    def __init__(self, matcher = matchers.All()):
        self.matcher_object = matcher

    def one_of(self, matcher1, matcher2):
        return QueryBuilder(matchers.And(matchers.Or(matcher1, matcher2), self.matcher_object))

    def plays_in(self, team):
        return QueryBuilder(matchers.And(matchers.PlaysIn(team), self.matcher_object))

    def has_at_least(self, value, attr):
        return QueryBuilder(matchers.And(matchers.HasAtLeast(value, attr), self.matcher_object))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(matchers.And(matchers.HasFewerThan(value, attr), self.matcher_object))

    def build(self):
        return self.matcher_object