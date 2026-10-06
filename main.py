from dotenv import load_dotenv

load_dotenv()

from src.writer import generate_post
from src.validator import validate_post
from src.critic import critique_post
from src.reviser import revise_post, fix_invalid_post
from src.publisher import publish_post
from src.logger import save_post_history
from src.scheduler import schedule_post


def main():
    print("=== AI Social Media Automation ===")

    topic = input("\nPost konusu: ")

    print("\nAI post oluşturuyor...")
    post = generate_post(topic)

    print("\n--- Generated Post ---")
    print(post)

    validation = validate_post(post)

    print("\n--- Validation Report ---")
    print(f"Karakter sayısı: {validation['character_count']}")
    print(f"Hashtag sayısı: {validation['hashtag_count']}")
    print(f"Durum: {'PASSED' if validation['valid'] else 'FAILED'}")

    if validation["errors"]:
        print("\nHatalar:")
        for error in validation["errors"]:
            print(f"- {error}")

    if validation["warnings"]:
        print("\nUyarılar:")
        for warning in validation["warnings"]:
            print(f"- {warning}")

    print("\nAI kalite değerlendirmesi yapıyor...")
    critique = critique_post(post)

    print("\n--- AI Critic Report ---")
    print(f"Clarity: {critique['clarity']}/10")
    print(f"Relevance: {critique['relevance']}/10")
    print(f"Professionalism: {critique['professionalism']}/10")
    print(f"Engagement: {critique['engagement']}/10")
    print(f"Suggestion: {critique['suggestion']}")

    print("\nAI postu revize ediyor...")
    revised_post = revise_post(post, critique)

    revised_validation = validate_post(revised_post)

    if not revised_validation["valid"]:
        print("\nRevize edilen post kuralları geçemedi.")
        print("Auto-Fix çalıştırılıyor...")

        revised_post = fix_invalid_post(
            revised_post,
            revised_validation["errors"],
        )

        revised_validation = validate_post(revised_post)

        print("\n--- Auto-Fixed Post ---")
        print(revised_post)

    print("\n--- Revised Post ---")
    print(revised_post)

    print("\n--- Final Validation ---")
    print(f"Karakter sayısı: {revised_validation['character_count']}")
    print(f"Hashtag sayısı: {revised_validation['hashtag_count']}")
    print(
        f"Durum: "
        f"{'PASSED' if revised_validation['valid'] else 'FAILED'}"
    )

    if not revised_validation["valid"]:
        print("\nPost validation başarısız.")
        print("Yayınlama işlemi engellendi.")
        return

    print("\n--- Publishing Mode ---")
    print("1 - Şimdi yayınla")
    print("2 - Zamanla")

    choice = input("\nSeçim: ").strip()

    if choice == "1":
        publish_result = publish_post(revised_post)
        save_post_history(publish_result)

        print("\n--- Publisher Report ---")
        print(f"Platform: {publish_result['platform']}")
        print(f"Status: {publish_result['status']}")
        print(f"Post ID: {publish_result['post_id']}")
        print(f"Published: {publish_result['published']}")
        print(f"Timestamp: {publish_result['timestamp']}")

    elif choice == "2":
        scheduled_time = input(
            "\nTarih ve saat (YYYY-MM-DD HH:MM): "
        )

        schedule_result = schedule_post(
            revised_post,
            scheduled_time,
        )

        if schedule_result["scheduled"]:
            print("\n--- Scheduler Report ---")
            print("Platform: X")
            print(f"Status: {schedule_result['status']}")
            print(
                f"Scheduled Time: "
                f"{schedule_result['scheduled_time']}"
            )
            print("Published: False")
        else:
            print("\nScheduler Error:")
            print(schedule_result["error"])

    else:
        print("\nGeçersiz seçim. Yayınlama işlemi yapılmadı.")


if __name__ == "__main__":
    main()