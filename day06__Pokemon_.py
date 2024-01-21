# 포켓몬 게임
# Reference : 포켓몬스터dp - 챔피언과 최종전



# 전체적인 흐름
#
# 1. 게임 시작
#   1) 1. Start 2. Quit   선택지에서 1 입력 시 게임 시작, 2 입력 시 게임 종료
#
#   2) 플레이어 이름 입력
#
# 2. 대화
#   1) 상대할 적과 간단한 대화 후 전투 진입
#
# 3. 전투
#   1) 적과의 전투 시작
#
#   2-1) 승리 시 -> 축하 메시지 출력
#
#   2-2) 패배 시 -> 패배 메시지 출력



# 필요 기능
#
# 1. UI
#   1) 진행을 위한 텍스트 메시지와 선택지
#
#   2) 전투 진입 시 행동 선택 화면
#       - 플레이어 남은 포켓몬 수
#         상대 남은 포켓몬 수
#       - 싸운다 -> 3-1) 으로
#       - 가방 ->
#       - 도망간다 -> 도망갈 수 없다는 메시지 출력
#       - 포켓몬 -> 포켓몬 교체(기절하지 않은 포켓몬만 가능)
#       - 추가내용 : 상성표
#
#   3-1) 싸운다 선택 시 화면
#       - 1.기술1  2.기술2  3.기술3  4.기술4  5.돌아간다   선택지에서 1 ~ 4 입력 시 선택한 번호의 스킬 발동, 5 입력 시 2) 화면으로 돌아가기
#
#   3-2) 가방 선택 시 화면
#       - 1.pp에이드(특정 포켓몬의 스킬 pp 5회복) 5개  2.회복약(hp 50회복) 10개  3.기력의 조각(기절한 포켓몬 부활 + hp 20회복) 3개  4.돌아간다
#       -   선택지에서 1 ~ 3 입력 시 선택한 번호의 아이템 사용, 4 입력 시 2) 화면으로 돌아가기
#       - 개수와 회복량은 밸런스에 따라 조정 가능

# 2. 포켓몬
#   1-1) 플레이어 포켓몬 종류
#       - 디아루가(타입 - 강철/드래곤, 약점 - 격투,땅, 강점 - 강철,노말,물,바위,벌레,비행,에스퍼,전기,풀(0.25배),독(무효), 기술 - 시간의포효,용의파동,화염방사,냉동빔)
#       - 뮤츠(타입 - 에스퍼, 약점 - 고스트,벌레,악, 강점 - 격투,에스퍼 기술 - HP회복,사이코키네시스,파동탄,냉동빔)
#       - 갸라도스(타입 - 비행/물, 약점 - 전기(4배), 강점 - 강철,격투,물,벌레,불꽃,땅(무효), 기술 - 폭포오르기,깨물어부수기,얼음엄니,용의춤)
#       - 로즈레이드(타입 - 독/풀, 약점 - 불꽃,비행,얼음,에스퍼, 강점 - 격투,물,전기,풀(0.25배), 기술 - 기가드레인,꽃잎댄스,오물폭탄,섀도볼)
#       - 한카리아스(타입 - 땅/드래곤, 약점 - 얼음(4배),드래곤, 강점 - 독,바위,불꽃,전기(무효), 기술 - 드래곤크루,지진,깨물어부수기,스톤에지)
#       - 피카츄(타입 - 전기, 약점 - 땅, 강점 - 전기,비행,강철, 기술 - 볼트태클,번개,아이언테일,전광석화)
#
#   1-2) 적 포켓몬 종류
#       - 난천 : 화강돌(레벨 - 61, 타입 - 고스트/악, 약점 - X)
#               트리토돈(레벨 - 60, 타입 - 물/땅, 약점 - 풀(4배))
#               루카리오(레벨 - 63, 타입 - 격투/강철, 약점 - 격투,땅,불꽃)
#               한카리아스(레벨 - 66, 타입 - 드래곤/땅, 약점 - 얼음(4배),드래곤)
#               밀로틱(레벨 - 63, 타입 - 물, 약점 - 풀,전기)
#               로즈레이드(레벨 - 60, 타입 - 풀/독, 약점 - 비행,불꽃,에스퍼,얼음)
#
#   2) hp
#   - 모든 포켓몬의 hp를 100으로 고정
#
#   3) pp
#   - 레퍼런스를 따름
#
#   4) 속성
#   - 레퍼런스를 따름
#
#   5) 레벨
#   - 플레이어 포켓몬의 레벨은 60으로 고정
#   - 적 포켓몬의 레벨은 레퍼런스를 따름
#
#
#
#
#

import random
class Pokemon() :
    def __init__(self, name, max_hp, cur_hp):
        self.name = name
        self.max_hp = max_hp
        self.cur_hp = max_hp

    def get_hp(self):
        return self.cur_hp

    def set_hp(self, cur_hp):
        if cur_hp <= 0 :
            print(f"{self.name}이 기절했습니다!")
            self.cur_hp = 0
        else :
            self.cur_hp = cur_hp


class Attack() :
    def __init__(self, name):
        self.name = name
        print("공격")

# 디아루가
class Dialga(Pokemon, Attack) :
    def __init__(self, name, max_hp, cur_hp):
        super().__init__(name, max_hp, cur_hp)

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) '시간의 포효' 공격!")

# 뮤츠
class Mewtwo(Pokemon, Attack) :
    def __init__(self, name, max_hp, cur_hp):
        super().__init__(name, max_hp, cur_hp)

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) '사이코 키네시스' 공격!")

# 갸라도스
class Gyarados(Pokemon, Attack) :
    def __init__(self, name, max_hp, cur_hp):
        super().__init__(name, max_hp, cur_hp)

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) '하이드로 펌프' 공격!")

# 로즈레이드
class Roserade(Pokemon, Attack) :
    def __init__(self, name, max_hp, cur_hp):
        super().__init__(name, max_hp, cur_hp)

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) '꽃잎댄스' 공격!")

# 한카리아스
class Garchomp(Pokemon, Attack) :
    def __init__(self, name, max_hp, cur_hp):
        super().__init__(name, max_hp, cur_hp)

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) '드래곤크루' 공격!")

# 피카츄
class Pikachu(Pokemon, Attack) :
    def __init__(self, name, max_hp, cur_hp):
        super().__init__(name, max_hp, cur_hp)

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) '볼트태클' 공격!")

# 플레이어 포켓몬
dialga1 = Dialga("디아루가", 100, 100)
mewtwo1 = Mewtwo("뮤츠", 100, 100)
gyarados1 = Gyarados("갸라도스", 100, 100)
roserade1 = Roserade("로즈레이드", 100, 100)
garchomp1 = Garchomp("한카리아스", 100, 100)
pikachu1 = Pikachu("피카츄", 100, 100)
player_pokemon_list = [dialga1, mewtwo1, gyarados1, roserade1, garchomp1, pikachu1]

#dialga1.attack(garchomp1)
#pikachu1.attack(garchomp1)

# 적 포켓몬
dialga2 = Dialga("디아루가2", 100, 100)
mewtwo2 = Mewtwo("뮤츠2", 100, 100)
gyarados2 = Gyarados("갸라도스2", 100, 100)
roserade2 = Roserade("로즈레이드2", 100, 100)
garchomp2 = Garchomp("한카리아스2", 100, 100)
pikachu2 = Pikachu("피카츄2", 100, 100)
enemy_pokemon_list = [dialga2, mewtwo2, gyarados2, roserade2, garchomp2, pikachu2]

# 게임 시작
is_start = False
while True :
    start = int(input("게임을 시작하시겠습니까?\n1. 예     2. 아니오\n"))
    if start == 1 :
        is_start = True
        break
    elif start == 2 :
        print("게임이 종료되었습니다.")
        break
    else:
        print("잘못된 입력입니다")

if is_start == True :
    # 플레이어 이름 입력
    player_name = input("플레이어 이름을 입력해주세요 : ")
    print(f"반갑습니다 {player_name}님! {player_name}님이 사용하실 포켓몬입니다.")
    print(f"1. {dialga1.name}   2. {mewtwo1.name}   3. {gyarados1.name}   4. {roserade1.name}   5. {garchomp1.name}   6. {pikachu1.name}")
    print(f"상대할 적은 챔피언 난천입니다.")
    print(f"전투 진입!")

    # 전투

    turn = 0
    game_over = False
    # 현재 포켓몬
    player_cur_pokemon = player_pokemon_list[0]
    enemy_cur_pokemon = enemy_pokemon_list[5]
    # 남은 포켓몬 수
    player_cur_remain = 6
    enemy_cur_remain = 6
    # 다음 포켓몬
    player_pokemon_idx = 0
    enemy_pokemon_idx = 5

    # 게임이 종료되지 않는다면 전투상황 반복
    while game_over == False :
        if player_cur_remain <= 0 :
            print(f"{player_name}은(는) 눈앞이 깜깜해졌다!")
            game_over = True
        elif enemy_cur_remain <= 0 :
            print("축하드립니다! 새로운 챔피언이 되셨습니다!")
            game_over = True

        # 자신의 턴일 때
        if(turn % 2 == 0) :
            act_choice_main = True
            print(f"{player_name}님의 턴 입니다.")
            act = int(input(f"행동을 선택하세요.\n1. 싸운다   2. 가방   3. 포켓몬   4. 도망간다\n"))
            # 싸운다 선택 시
            if (act == 1):
                print(f"난천 현재 포켓몬 : {enemy_cur_pokemon.name}")
                print(f"현재 포켓몬 : {player_cur_pokemon.name}")
                # 공격 실행
                player_cur_pokemon.attack(enemy_cur_pokemon)
                # 랜덤 데미지 설정
                random_dmg = random.randint(1, 100)
                print(f"적 {enemy_cur_pokemon.name}에게 {random_dmg}만큼의 피해를 입혔습니다!")
                enemy_cur_pokemon.set_hp(enemy_cur_pokemon.cur_hp - random_dmg)
                print(f"적 {enemy_cur_pokemon.name}의 현재 체력은 {enemy_cur_pokemon.cur_hp}입니다.")
                if enemy_cur_pokemon.cur_hp <= 0 :
                    enemy_cur_remain -= 1
                    enemy_pokemon_idx -= 1
                    if enemy_pokemon_idx < 0:
                        print("축하드립니다! 새로운 챔피언이 되셨습니다!")
                        game_over = True
                        break
                    enemy_cur_pokemon = enemy_pokemon_list[enemy_pokemon_idx]
                    print(f"난천이 새로운 포켓몬 {enemy_cur_pokemon.name}을(를) 내보냈습니다!")
                    print(f"난천의 남은 포켓몬은 {enemy_cur_remain}마리 입니다.")
                turn += 1
            elif (act == 2):
                print("현재 이용할 수 없습니다")
                turn += 1
            elif (act == 3):
                print("현재 이용할 수 없습니다")
                turn += 1
            else:
                print("지금은 도망갈 수 없습니다")
        else :
            print(f"난천의 턴 입니다.")
            enemy_cur_pokemon.attack(player_cur_pokemon)
            random_dmg = random.randint(1, 100)
            print(f"{player_cur_pokemon.name}이(가) {random_dmg}만큼의 피해를 입었습니다!")
            player_cur_pokemon.set_hp(player_cur_pokemon.cur_hp - random_dmg)
            print(f"플레이어 {player_cur_pokemon.name}의 현재 체력은 {player_cur_pokemon.cur_hp}입니다.")
            if  player_cur_pokemon.cur_hp <= 0:
                player_cur_remain -= 1
                player_pokemon_idx += 1
                if player_pokemon_idx > 5 :
                    print(f"{player_name}은(는) 눈앞이 깜깜해졌다!")
                    game_over = True
                    break
                player_cur_pokemon = player_pokemon_list[player_pokemon_idx]
                print(f"{player_name}님이 새로운 포켓몬 {player_cur_pokemon.name}을(를) 내보냈습니다!")
                print(f"{player_name}님의 남은 포켓몬은 {player_cur_remain}마리 입니다.")
            turn += 1
