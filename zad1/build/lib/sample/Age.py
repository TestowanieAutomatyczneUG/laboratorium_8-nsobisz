
class Age:
    def how_old(self, number, word):
        if (type(number) == int and type(word) == str) or (type(number) == str and type(word) == str):
            try:
                a = int(number)
                b = word.lower()
                if a < 0:
                    raise Exception("Błąd, drugi argument musi być większy od zera")
                elif b not in ["ziemia", "wenux", "mars", "saturn", "jowisz", "uran","neptun","merkury"]:
                    raise Exception("Błąd, pierwszy argument musi być nazwą planety")
                else:
                    p = 31557600
                    if b == "ziemia":
                        return (round(a / p, 2))
                    elif b == "merkury":
                        return (round(a / (p * 0.2408467), 2))
                    elif b == "wenus":
                        return (round(a / (p * 0.61519726), 2))
                    elif b == "mars":
                        return (round(a / (p * 1.8808158), 2))
                    elif b == "jowisz":
                        return (round(a / (p * 11.862615), 2))
                    elif b == "saturn":
                        return (round(a / (p * 29.447498), 2))
                    elif b == "uran":
                        return (round(a / (p * 84.016846), 2))
                    elif b == "neptun":
                        return (round(a / (p * 164.79132), 2))
            except ValueError:
                raise Exception("Błąd, drugi argument jest stringiem")
        elif type(word) != str and type(number) != int:
            raise Exception("Błąd, argumenty są złego typu danych")


print(Age().how_old(890245364,"uran"))