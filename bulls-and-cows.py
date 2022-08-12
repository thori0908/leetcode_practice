class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counters_secret = [0] * 10
        counters_guess = [0] * 10

        bulls = 0

        for index, secret_letter in enumerate(secret):
            secret_number = int(secret_letter)
            guess_number = int(guess[index])
            counters_secret[secret_number] += 1
            counters_guess[guess_number] += 1

            if secret_number == guess_number:
                bulls += 1
                counters_secret[guess_number] -= 1
                counters_guess[guess_number] -= 1

        cows = 0
        for index, counter in enumerate(counters_secret):
            cows = cows + min(counters_secret[index], counters_guess[index])

        return str(bulls)+'A'+str(cows)+'B'