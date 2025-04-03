import random

class Deck:

  def __init__(self, num_lands):
    self.cards = []
    for i in range(100):
      if i < num_lands:
        self.cards.append(1)
      else:
        self.cards.append(0)
    random.shuffle(self.cards)

  def draw(self):
    return self.cards.pop()

  def __str__(self):
    return f"{self.cards}"

class Test:

  def __init__(self, num_lands, target_lands, total_cards_drawn):
    self.num_lands = num_lands
    self.target_lands = target_lands
    self.total_cards_drawn = total_cards_drawn

  def run(self) -> bool:
    deck = Deck(self.num_lands)

    num_lands_drawn = 0
    for i in range(self.total_cards_drawn):
      card = deck.draw()
      num_lands_drawn += card

    # print(f"{num_lands_drawn} >= {self.target_lands}")

    return num_lands_drawn >= self.target_lands

class Scenario:

  def __init__(self, num_lands, target_lands, total_cards_drawn):
    self.num_lands = num_lands
    self.target_lands = target_lands
    self.total_cards_drawn = total_cards_drawn
   
  def run(self, num_tests) -> float:

    tests_passed = 0
    for i in range(num_tests):
      test = Test(self.num_lands, self.target_lands, self.total_cards_drawn)
      result = test.run()
      if result:
        tests_passed += 1

    return round((100 * tests_passed) / num_tests, 2)
      
class ScenarioFactory:

  def __init__(self, commander_cost):
    self.commander_cost = commander_cost

  def build(self, num_lands):
    target_lands = self.commander_cost
    # Starting hand of 7, 3 mulligan, and draw one card per turn until commander can be cast
    total_cards_drawn = 7 + 3 + self.commander_cost
    return Scenario(num_lands, target_lands, total_cards_drawn)

class LandCounter:

  def run(self):
    for commander_cost in range(2,7):
      scenario_factory = ScenarioFactory(commander_cost)
      print(f"Commander Cost {commander_cost}")
      for num_lands in range(30, 46):
        scenario = scenario_factory.build(num_lands)
        result = scenario.run(3001)
        
        print(f"  Lands: {num_lands}, result {result}")
      
def main():
  land_counter = LandCounter()
  land_counter.run()

main()
