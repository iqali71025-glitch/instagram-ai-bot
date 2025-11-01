#!/usr/bin/env python3
"""
Instagram AI Bot - نظام الذكاء الاصطناعي لإدارة المحتوى
يعمل على GitHub Actions
"""

import random
import json
from datetime import datetime
import os

class InstagramAIBot:
    def __init__(self):
        self.setup_content_library()
        self.execution_log = []
        
    def setup_content_library(self):
        """إعداد مكتبة المحتوى"""
        self.content_ideas = {
            'ميمز': [
                "عندما تطلب توصيل وياك 5 أصدقاء 😂",
                "الفرق بين نوم Weekend والـ Weekday 🛌",
                "ردود فعل الأم عندما تطلب منها شي 🏃‍♂️",
                "عندما تفتح الثلاجة 10 مرات وانت ما تدري شتبي 🧃"
            ],
            'نصيحة': [
                "💡 نصيحة لزيادة إنتاجيتك: ابدأ صغير واستمر",
                "🚀 كيف تحقق أهدافك في 30 يوم؟ خطوة بخطوة",
                "🎯 سر النجاح في إدارة الوقت ⏰",
                "🌟 3 عادات غيرت حياتي للأفضل"
            ],
            'سؤال': [
                "🤔 شو رأيكم في التحديات الجديدة؟",
                "❓ أي نوع محتوى تفضلون تشوفون؟",
                "💭 لو خيروك بين السفر والعمل، تختار أي؟",
                "🎪 متى آخر مرة ضحكت من قلبك؟"
            ],
            'تحدي': [
                "🎯 تحدى 7 أيام للإبداع! هل أنت مستعد؟",
                "🏆 شارك في تحدي القراءة لمدة 21 يوم 📚",
                "💪 تحدي الرياضة الصباحية - اليوم الأول",
                "🚀 تحدى نفسك بتعلم مهارة جديدة"
            ],
            'اقتباس': [
                "«النجاح رحلة وليس وجهة» - استمتع بالطريق ✨",
                "«الأحلام تتحقق بالعمل لا بالأمنيات» 🌟",
                "«كل كبير بدأ صغيراً» - لا تستعجل النتائج 🚀",
                "«التحديات تصنع الأبطال» - واجه الصعوبات 💪"
            ]
        }
        
        self.hashtags_library = {
            'عام': ['#منشن_لصاحبك', '#لايك_واشتراك', '#تصميمي', '#فولو'],
            'ميمز': ['#ميمز', '#ضحك', '#كوميديا', '#سوالف', '#ترفيه'],
            'نصيحة': ['#نصيحة', '#تطوير_ذات', '#معلومة', '#فائدة'],
            'سؤال': ['#سؤال', '#رأيكم', '#نقاش', '#تفاعل'],
            'محلي': ['#السعودية', '#الرياض', '#الخليج', '#دبي']
        }
    
    def generate_content(self, content_type=None):
        """توليد محتوى ذكي"""
        if not content_type:
            content_type = random.choice(list(self.content_ideas.keys()))
        
        idea = random.choice(self.content_ideas[content_type])
        
        # توليد هاشتاقات ذكية
        base_tags = self.hashtags_library['عام']
        type_tags = self.hashtags_library.get(content_type, [])
        local_tags = self.hashtags_library['محli']
        
        all_tags = base_tags + type_tags + local_tags
        selected_tags = ' '.join(random.sample(all_tags, min(8, len(all_tags))))
        
        return {
            'type': content_type,
            'idea': idea,
            'hashtags': selected_tags,
            'best_time': self.suggest_best_time(),
            'success_chance': random.randint(80, 95)
        }
    
    def suggest_best_time(self):
        """اقتراح أفضل وقت للنشر"""
        times = [
            "8:00-10:00 صباحاً ☀️",
            "12:00-2:00 ظهراً 🍽️", 
            "4:00-6:00 مساءاً 🌇",
            "8:00-10:00 مساءاً 🌙"
        ]
        return random.choice(times)
    
    def simulate_post(self, post_type):
        """محاكاة نشر على انستقرام"""
        content = self.generate_content()
        
        # محاكاة النجاح/الفشل
        success_rate = 0.85 if post_type == 'reel' else 0.90
        success = random.random() < success_rate
        
        result = {
            'post_type': post_type,
            'content_type': content['type'],
            'idea': content['idea'],
            'hashtags': content['hashtags'],
            'best_time': content['best_time'],
            'success': success,
            'engagement': random.randint(70, 95),
            'timestamp': datetime.now().isoformat()
        }
        
        self.execution_log.append(result)
        return result
    
    def run_daily_schedule(self):
        """تشغيل الجدولة اليومية"""
        print("🚀 بدء تشغيل بوت انستقرام الذكي...")
        print(f"🕒 وقت التشغيل: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        # تحديد المهام بناءً على الوقت
        current_time = datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        
        posts = []
        
        # رييلات (9:00, 3:00, 9:00 م)
        if current_hour in [6, 12, 18] and current_minute == 0:
            posts.append(('reel', '🎬 نشر رييل'))
        
        # ستوريات (10:30, 1:30, 4:30, 7:30, 11:30 م)
        if current_hour in [7, 10, 13, 16, 20] and current_minute == 30:
            posts.append(('story', '📱 نشر ستوري'))
        
        # إذا لم يكن وقت مجدول، ننشر عشوائياً
        if not posts and random.random() < 0.4:
            post_type = random.choice(['reel', 'story'])
            posts.append((post_type, f'🎲 نشر {post_type} عشوائي'))
        
        # تنفيذ المهام
        for post_type, description in posts:
            print(f"\n{description}:")
            result = self.simulate_post(post_type)
            
            status_emoji = "✅" if result['success'] else "❌"
            print(f"   {status_emoji} {result['idea']}")
            print(f"   🏷️ {result['hashtags']}")
            print(f"   ⭐ تفاعل: {result['engagement']}%")
            print(f"   ⏰ وقت مقترح: {result['best_time']}")
        
        # إحصائيات
        successful_posts = sum(1 for post in self.execution_log if post['success'])
        total_posts = len(self.execution_log)
        
        print(f"\n📊 إحصائيات اليوم:")
        print(f"   📈 النجاح: {successful_posts}/{total_posts}")
        print(f"   📋 معدل النجاح: {int((successful_posts/total_posts)*100) if total_posts > 0 else 0}%")
        
        # حفظ السجل
        self.save_execution_log()
        
        return len(posts)
    
    def save_execution_log(self):
        """حفظ سجل التنفيذ"""
        log_data = {
            'total_executions': len(self.execution_log),
            'successful_posts': sum(1 for post in self.execution_log if post['success']),
            'last_update': datetime.now().isoformat(),
            'executions': self.execution_log[-50:]  # آخر 50 تنفيذ
        }
        
        with open('execution_history.json', 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)

def main():
    """الدالة الرئيسية"""
    bot = InstagramAIBot()
    posts_count = bot.run_daily_schedule()
    
    print(f"\n🎉 اكتمل التشغيل بنجاح!")
    print(f"📤 تم معالجة {posts_count} منشور")
    print(f"💾 تم حفظ السجل في execution_history.json")

if __name__ == "__main__":
    main()
