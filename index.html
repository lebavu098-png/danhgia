<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đánh Giá Tình Trạng Nghiện Game (DSM-5) & Cân Bằng Cuộc Sống</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Canvas Confetti CDN -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts Inter & Orbitron -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@600;800;900&display=swap" rel="stylesheet">
    <!-- QRCode JS Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        tech: ['Orbitron', 'sans-serif'],
                    },
                    colors: {
                        neonCyan: '#00f3ff',
                        neonPurple: '#9d00ff',
                        neonPink: '#ff0055',
                        neonGreen: '#00ff66',
                        cyberDark: '#0a0f1d',
                        cyberCard: '#12192d',
                    },
                    boxShadow: {
                        'glow-cyan': '0 0 20px rgba(0, 243, 255, 0.35)',
                        'glow-purple': '0 0 20px rgba(157, 0, 255, 0.35)',
                        'glow-pink': '0 0 25px rgba(255, 0, 85, 0.45)',
                        'glow-amber': '0 0 20px rgba(245, 158, 11, 0.35)',
                    }
                }
            }
        }
    </script>

    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #060913;
            color: #f1f5f9;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(0, 243, 255, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 85% 85%, rgba(157, 0, 255, 0.07) 0%, transparent 40%);
            background-attachment: fixed;
        }

        .font-tech {
            font-family: 'Orbitron', sans-serif;
        }

        /* Glassmorphism Styles */
        .glass-card {
            background: rgba(18, 25, 45, 0.75);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }

        .glass-card-hover {
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .glass-card-hover:hover {
            border-color: rgba(0, 243, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0, 243, 255, 0.12);
        }

        /* Slide Animation for Questions */
        .question-slide-in {
            animation: slideInRight 0.35s ease-out forwards;
        }
        .question-slide-back {
            animation: slideInLeft 0.35s ease-out forwards;
        }

        @keyframes slideInRight {
            from { opacity: 0; transform: translateX(30px); }
            to { opacity: 1; transform: translateX(0); }
        }

        @keyframes slideInLeft {
            from { opacity: 0; transform: translateX(-30px); }
            to { opacity: 1; transform: translateX(0); }
        }

        /* Selection Pulse Effect */
        @keyframes pulseGlow {
            0% { box-shadow: 0 0 0 0 rgba(0, 243, 255, 0.4); }
            70% { box-shadow: 0 0 0 12px rgba(0, 243, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 243, 255, 0); }
        }
        .option-selected-pulse {
            animation: pulseGlow 0.6s ease-out;
        }

        /* Checkmark Rotation Effect */
        .check-icon-spin {
            animation: checkSpin 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        }
        @keyframes checkSpin {
            0% { transform: scale(0) rotate(-90deg); opacity: 0; }
            100% { transform: scale(1) rotate(0deg); opacity: 1; }
        }

        /* Red Alarm Pulse for Severe Addiction */
        @keyframes alarmPulse {
            0%, 100% { border-color: rgba(255, 0, 85, 0.8); box-shadow: 0 0 15px rgba(255, 0, 85, 0.4); }
            50% { border-color: rgba(255, 0, 85, 0.3); box-shadow: 0 0 35px rgba(255, 0, 85, 0.7); }
        }
        .severe-alarm-card {
            animation: alarmPulse 2s infinite ease-in-out;
        }

        /* Toast Animation */
        @keyframes toastUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-toast {
            animation: toastUp 0.3s ease-out forwards;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #060913; }
        ::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #00f3ff; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-neonCyan selection:text-black">

    <!-- Toast Notification Container -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 hidden bg-slate-900 border border-neonCyan text-white px-5 py-3 rounded-xl shadow-glow-cyan flex items-center space-x-3 animate-toast">
        <i class="fa-solid fa-circle-check text-neonCyan text-lg"></i>
        <span id="toast-message" class="text-xs sm:text-sm font-semibold">Đã sao chép liên kết vào bộ nhớ tạm!</span>
    </div>

    <!-- Header Navigation Bar -->
    <header class="sticky top-0 z-40 glass-card border-b border-slate-800/80 px-4 lg:px-8 py-3">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
            
            <!-- Logo -->
            <div class="flex items-center space-x-3 cursor-pointer" onclick="switchTab('assessment')">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 via-indigo-600 to-purple-600 flex items-center justify-center text-white shadow-glow-cyan">
                    <i class="fa-solid fa-gamepad text-lg"></i>
                </div>
                <div>
                    <h1 class="font-tech font-bold text-base sm:text-lg leading-tight bg-gradient-to-r from-neonCyan via-indigo-300 to-neonPurple bg-clip-text text-transparent">
                        MIND-BALANCE
                    </h1>
                    <p class="text-[10px] sm:text-xs text-slate-400">Đánh giá Nghiện Game DSM-5 Chi Tiết</p>
                </div>
            </div>

            <!-- Desktop Nav Tabs -->
            <nav class="hidden md:flex space-x-1 bg-slate-950/80 p-1 rounded-xl border border-slate-800">
                <button onclick="switchTab('assessment')" id="nav-assessment" class="nav-btn px-4 py-2 rounded-lg text-xs font-semibold text-neonCyan bg-slate-800/90 transition-all flex items-center">
                    <i class="fa-solid fa-clipboard-check mr-2"></i>Đánh giá DSM-5
                </button>
                <button onclick="switchTab('calculator')" id="nav-calculator" class="nav-btn px-4 py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-slate-200 transition-all flex items-center">
                    <i class="fa-solid fa-chart-pie mr-2"></i>Phân bổ thời gian
                </button>
                <button onclick="switchTab('planner')" id="nav-planner" class="nav-btn px-4 py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-slate-200 transition-all flex items-center">
                    <i class="fa-solid fa-bullseye mr-2"></i>Mục tiêu & Thói quen
                </button>
                <button onclick="switchTab('support')" id="nav-support" class="nav-btn px-4 py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-slate-200 transition-all flex items-center">
                    <i class="fa-solid fa-heart-pulse mr-2 text-rose-500"></i>Hỗ trợ tâm lý
                </button>
            </nav>

            <!-- Mobile Menu Toggle Button -->
            <button onclick="toggleMobileMenu()" class="md:hidden text-slate-300 hover:text-white p-2 rounded-lg bg-slate-900 border border-slate-800">
                <i class="fa-solid fa-bars text-lg"></i>
            </button>
        </div>

        <!-- Mobile Navigation Menu Dropdown -->
        <div id="mobile-menu" class="hidden md:hidden mt-3 pt-3 border-t border-slate-800/80 flex flex-col space-y-2">
            <button onclick="switchTab('assessment'); toggleMobileMenu()" class="px-4 py-2.5 rounded-lg text-left text-xs font-semibold text-slate-200 bg-slate-900/80 flex items-center">
                <i class="fa-solid fa-clipboard-check w-6 text-neonCyan"></i>Bài Đánh Giá DSM-5
            </button>
            <button onclick="switchTab('calculator'); toggleMobileMenu()" class="px-4 py-2.5 rounded-lg text-left text-xs font-semibold text-slate-200 bg-slate-900/80 flex items-center">
                <i class="fa-solid fa-chart-pie w-6 text-indigo-400"></i>Phân Bổ Quỹ Thời Gian
            </button>
            <button onclick="switchTab('planner'); toggleMobileMenu()" class="px-4 py-2.5 rounded-lg text-left text-xs font-semibold text-slate-200 bg-slate-900/80 flex items-center">
                <i class="fa-solid fa-bullseye w-6 text-emerald-400"></i>Kế Hoạch & Thói Quen
            </button>
            <button onclick="switchTab('support'); toggleMobileMenu()" class="px-4 py-2.5 rounded-lg text-left text-xs font-semibold text-slate-200 bg-slate-900/80 flex items-center">
                <i class="fa-solid fa-heart-pulse w-6 text-rose-500"></i>Tư Vấn Tâm Lý Khẩn Cấp
            </button>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="max-w-4xl mx-auto px-4 py-6 sm:py-10 w-full flex-grow">

        <!-- TAB 1: ASSESSMENT QUIZ STEPPER -->
        <section id="tab-assessment" class="tab-content space-y-6">
            
            <!-- Quiz Intro Hero Banner -->
            <div id="quiz-intro" class="glass-card rounded-2xl p-6 sm:p-10 relative overflow-hidden">
                <div class="absolute -right-12 -top-12 w-56 h-56 bg-neonCyan/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute -left-12 -bottom-12 w-56 h-56 bg-neonPurple/10 rounded-full blur-3xl pointer-events-none"></div>

                <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-cyan-500/10 text-neonCyan text-xs font-semibold mb-4 border border-cyan-500/20">
                    <i class="fa-solid fa-brain"></i>
                    <span>Chuẩn Chẩn Đoán Lâm Sàng DSM-5 (Internet Gaming Disorder)</span>
                </div>

                <h2 class="text-2xl sm:text-4xl font-extrabold mb-4 text-white leading-tight">
                    Tầm Soát Chi Tiết Tình Trạng Nghiện Game
                </h2>

                <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6 max-w-2xl">
                    Bài trắc nghiệm gồm <b class="text-neonCyan">9 tiêu chí lâm sàng chuẩn quốc tế</b>. Trong quá trình trả lời, điểm số sẽ được ẩn hoàn toàn để bạn có câu trả lời trung thực và khách quan nhất. Bản phân tích sâu sẽ xuất hiện ngay sau khi bạn hoàn thành.
                </p>

                <div class="flex flex-wrap gap-4 items-center">
                    <button onclick="startQuiz()" class="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-gradient-to-r from-cyan-500 via-indigo-600 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white font-bold text-sm tracking-wide shadow-glow-cyan transition-all transform active:scale-95 flex items-center justify-center space-x-2">
                        <span>BẮT ĐẦU ĐÁNH GIÁ</span>
                        <i class="fa-solid fa-arrow-right text-xs"></i>
                    </button>
                    <span class="text-xs text-slate-400 flex items-center justify-center w-full sm:w-auto">
                        <i class="fa-solid fa-shield-halved mr-1.5 text-neonCyan"></i> Không lưu tên • Hoàn toàn bảo mật
                    </span>
                </div>
            </div>

            <!-- Quiz Stepper Wizard Container (Hidden initially) -->
            <div id="quiz-container" class="hidden glass-card rounded-2xl p-5 sm:p-8 space-y-6">
                
                <!-- Progress Header (NO SCORE DISPLAYED HERE) -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-xs font-semibold">
                        <span id="question-tracker" class="text-slate-300 font-tech">CÂU HỎI 01 / 09</span>
                        <span id="progress-percent" class="text-neonCyan font-bold">11% Hoàn thành</span>
                    </div>
                    
                    <!-- Progress Bar -->
                    <div class="w-full h-3 bg-slate-900 rounded-full overflow-hidden p-0.5 border border-slate-800">
                        <div id="progress-bar" class="h-full bg-gradient-to-r from-neonCyan via-indigo-500 to-neonPurple rounded-full transition-all duration-300 w-[11%]"></div>
                    </div>
                </div>

                <!-- Question Slide Box -->
                <div id="question-box" class="py-2 transition-all">
                    <span id="question-category" class="inline-block text-[11px] font-bold uppercase tracking-widest text-neonCyan px-2.5 py-1 rounded-md bg-cyan-950/60 border border-cyan-800/50 mb-3">
                        1. Bận tâm quá mức (Preoccupation)
                    </span>
                    <h3 id="question-text" class="text-lg sm:text-2xl font-bold text-white leading-relaxed">
                        --
                    </h3>
                </div>

                <!-- Options List (Yes / No) -->
                <div class="grid grid-cols-1 gap-3.5" id="options-container">
                    <!-- Dynamic Options -->
                </div>

                <!-- Navigation Controls Footer -->
                <div class="flex items-center justify-between pt-5 border-t border-slate-800/80">
                    <!-- Prev Button -->
                    <button id="btn-prev" onclick="prevQuestion()" disabled class="px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 text-xs sm:text-sm font-semibold transition-all disabled:opacity-30 disabled:cursor-not-allowed flex items-center space-x-2 active:scale-95">
                        <i class="fa-solid fa-chevron-left text-xs"></i>
                        <span>Quay lại</span>
                    </button>

                    <div class="text-xs text-slate-500 hidden sm:block italic">
                        Chọn đáp án phản ánh đúng nhất thực tế của bạn
                    </div>

                    <!-- Next or Submit Button -->
                    <button id="btn-next" onclick="nextQuestion()" disabled class="px-6 py-2.5 rounded-xl bg-slate-800 text-slate-500 text-xs sm:text-sm font-bold transition-all disabled:opacity-40 disabled:cursor-not-allowed flex items-center space-x-2 active:scale-95">
                        <span id="btn-next-text">Đi tiếp</span>
                        <i id="btn-next-icon" class="fa-solid fa-chevron-right text-xs"></i>
                    </button>
                </div>
            </div>

            <!-- Quiz Results View (Hidden initially) -->
            <div id="quiz-results" class="hidden space-y-6">
                
                <!-- Main Result Card -->
                <div id="result-main-card" class="glass-card rounded-2xl p-6 sm:p-10 text-center relative overflow-hidden">
                    <div class="inline-block px-3 py-1 rounded-full bg-slate-900 border border-slate-800 text-xs font-semibold text-slate-400 mb-2">
                        KẾT QUẢ ĐÁNH GIÁ LÂM SÀNG DSM-5
                    </div>

                    <h2 id="result-title" class="text-2xl sm:text-4xl font-extrabold mb-2 font-tech">--</h2>

                    <!-- Score Gauge Chart -->
                    <div class="relative w-56 h-36 mx-auto mt-4 mb-2 flex items-center justify-center">
                        <canvas id="gaugeChart" class="w-full h-full"></canvas>
                        <div class="absolute inset-x-0 bottom-2 flex flex-col items-center justify-center">
                            <span id="score-number" class="text-4xl font-black text-white tracking-tight">0</span>
                            <span class="text-xs text-slate-400 font-medium">/ 9 Tiêu chuẩn DSM-5</span>
                        </div>
                    </div>

                    <p id="result-description" class="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto leading-relaxed mb-6">
                        --
                    </p>

                    <!-- Action Buttons -->
                    <div class="flex flex-wrap justify-center gap-3">
                        <button onclick="restartQuiz()" class="px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 text-xs sm:text-sm font-semibold transition-all flex items-center space-x-2 active:scale-95">
                            <i class="fa-solid fa-rotate-left"></i>
                            <span>Làm Lại Bài Đánh Giá</span>
                        </button>
                        <button onclick="openShareModal()" class="px-6 py-2.5 rounded-xl bg-gradient-to-r from-neonCyan via-indigo-600 to-neonPurple text-white text-xs sm:text-sm font-extrabold shadow-glow-cyan transition-all flex items-center space-x-2 active:scale-95">
                            <i class="fa-solid fa-share-nodes text-base"></i>
                            <span>CHIA SẺ KẾT QUẢ NÀY</span>
                        </button>
                        <button onclick="downloadResultsReport()" class="px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 text-xs sm:text-sm font-semibold transition-all flex items-center space-x-2 active:scale-95">
                            <i class="fa-solid fa-download"></i>
                            <span>Tải File Báo Cáo (.txt)</span>
                        </button>
                    </div>
                </div>

                <!-- 4 DETAILED ASPECTS ANALYSIS BREAKDOWN -->
                <div class="glass-card rounded-2xl p-6 sm:p-8 space-y-4">
                    <h3 class="text-lg font-bold text-white flex items-center border-b border-slate-800 pb-3">
                        <i class="fa-solid fa-chart-bar text-neonCyan mr-2.5 text-xl"></i>
                        Phân Tích Chi Tiết Theo 4 Khía Cạnh Sức Khỏe & Hành Vi
                    </h3>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2" id="aspects-grid">
                        <!-- Aspect 1 -->
                        <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold uppercase tracking-wide text-cyan-400 flex items-center">
                                    <i class="fa-solid fa-brain mr-2"></i>1. Sức Khỏe Tâm Thần & Cảm Xúc
                                </span>
                                <span id="aspect-status-1" class="text-xs font-bold px-2 py-0.5 rounded bg-slate-900">--</span>
                            </div>
                            <p id="aspect-desc-1" class="text-xs text-slate-300 leading-relaxed">--</p>
                        </div>

                        <!-- Aspect 2 -->
                        <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold uppercase tracking-wide text-purple-400 flex items-center">
                                    <i class="fa-solid fa-users mr-2"></i>2. Mối Quan Hệ & Xã Hội
                                </span>
                                <span id="aspect-status-2" class="text-xs font-bold px-2 py-0.5 rounded bg-slate-900">--</span>
                            </div>
                            <p id="aspect-desc-2" class="text-xs text-slate-300 leading-relaxed">--</p>
                        </div>

                        <!-- Aspect 3 -->
                        <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold uppercase tracking-wide text-emerald-400 flex items-center">
                                    <i class="fa-solid fa-briefcase mr-2"></i>3. Hiệu Suất Học Tập / Công Việc
                                </span>
                                <span id="aspect-status-3" class="text-xs font-bold px-2 py-0.5 rounded bg-slate-900">--</span>
                            </div>
                            <p id="aspect-desc-3" class="text-xs text-slate-300 leading-relaxed">--</p>
                        </div>

                        <!-- Aspect 4 -->
                        <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold uppercase tracking-wide text-amber-400 flex items-center">
                                    <i class="fa-solid fa-sliders mr-2"></i>4. Tự Kiểm Soát & Giải Tỏa Cảm Xúc
                                </span>
                                <span id="aspect-status-4" class="text-xs font-bold px-2 py-0.5 rounded bg-slate-900">--</span>
                            </div>
                            <p id="aspect-desc-4" class="text-xs text-slate-300 leading-relaxed">--</p>
                        </div>
                    </div>
                </div>

                <!-- PERSONALIZED STRATEGY RECOMMENDATIONS -->
                <div class="glass-card rounded-2xl p-6 sm:p-8 space-y-4">
                    <h3 class="text-lg font-bold text-white flex items-center">
                        <i class="fa-solid fa-compass text-amber-400 mr-2.5 text-xl"></i>
                        Chiến Lược Can Thiệp & Lời Khuyên Chuyên Môn
                    </h3>
                    <div id="recommendations-content" class="space-y-3 text-sm text-slate-300">
                        <!-- Filled dynamically -->
                    </div>
                </div>

            </div>

        </section>

        <!-- TAB 2: TIME CALCULATOR & PIE CHART -->
        <section id="tab-calculator" class="tab-content hidden space-y-6">
            <div class="glass-card rounded-2xl p-6 sm:p-8">
                <div class="max-w-2xl mb-6">
                    <h2 class="text-xl sm:text-2xl font-bold text-white mb-2 font-tech">Bảng Tính Quỹ Thời Gian Trong Ngày</h2>
                    <p class="text-slate-400 text-sm leading-relaxed">
                        Nhập số giờ trung bình dành cho từng hoạt động (tổng 24h). Biểu đồ giúp bạn hình dung rõ tỷ lệ cuộc sống đang dành cho thế giới ảo.
                    </p>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                    <div class="lg:col-span-6 space-y-4">
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-neonCyan mb-1.5">🎮 Chơi Game (Giờ/ngày)</label>
                            <input type="number" id="time-gaming" value="4" min="0" max="24" step="0.5" oninput="updateTimeChart()" class="w-full bg-slate-950 border border-slate-700 focus:border-neonCyan rounded-xl px-4 py-3 text-white focus:outline-none transition-all font-semibold">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-indigo-400 mb-1.5">😴 Ngủ & Nghỉ ngơi (Giờ/ngày)</label>
                            <input type="number" id="time-sleep" value="7" min="0" max="24" step="0.5" oninput="updateTimeChart()" class="w-full bg-slate-950 border border-slate-700 focus:border-indigo-500 rounded-xl px-4 py-3 text-white focus:outline-none transition-all font-semibold">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-emerald-400 mb-1.5">📚 Học tập / Làm việc (Giờ/ngày)</label>
                            <input type="number" id="time-work" value="7" min="0" max="24" step="0.5" oninput="updateTimeChart()" class="w-full bg-slate-950 border border-slate-700 focus:border-emerald-500 rounded-xl px-4 py-3 text-white focus:outline-none transition-all font-semibold">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-amber-400 mb-1.5">⚽ Thể thao, Bạn bè & Khác (Giờ/ngày)</label>
                            <input type="number" id="time-social" value="2" min="0" max="24" step="0.5" oninput="updateTimeChart()" class="w-full bg-slate-950 border border-slate-700 focus:border-amber-500 rounded-xl px-4 py-3 text-white focus:outline-none transition-all font-semibold">
                        </div>

                        <div id="time-warning" class="hidden p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs font-medium">
                            <i class="fa-solid fa-triangle-exclamation mr-1"></i> Tổng thời gian vượt quá 24h. Vui lòng kiểm tra lại số giờ nhập!
                        </div>
                    </div>

                    <div class="lg:col-span-6 flex flex-col items-center justify-center p-6 bg-slate-950/60 rounded-2xl border border-slate-800">
                        <div class="w-60 h-60 relative">
                            <canvas id="timeDistributionChart"></canvas>
                        </div>
                        <div class="mt-4 text-center">
                            <span class="text-xs text-slate-400 block">Tỷ lệ thời gian chơi game:</span>
                            <span id="gaming-pct-val" class="text-2xl font-black text-neonCyan font-tech">16.7% cuộc sống</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- TAB 3: HABITS & ACTION PLANNER -->
        <section id="tab-planner" class="tab-content hidden space-y-6">
            <div class="glass-card rounded-2xl p-6 sm:p-8">
                <h2 class="text-xl sm:text-2xl font-bold text-white mb-2 font-tech">Xây Dựng Thói Quên Kiểm Soát Game</h2>
                <p class="text-slate-400 text-sm mb-6">
                    Đánh dấu chọn những hành động nhỏ bạn cam kết thực hiện từ hôm nay để từng bước lấy lại sự chủ động:
                </p>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5" id="habits-list">
                    <!-- Dynamic Habits List -->
                </div>

                <div class="mt-8 p-5 rounded-2xl bg-gradient-to-r from-cyan-950/60 via-slate-900 to-purple-950/60 border border-cyan-500/20 flex flex-col sm:flex-row justify-between items-center gap-4">
                    <div>
                        <h4 class="font-bold text-white text-sm sm:text-base">Tiến độ cam kết cá nhân</h4>
                        <p class="text-xs text-slate-300" id="habit-progress-text">Đã chọn 0 / 6 mục tiêu</p>
                    </div>
                    <div class="w-full sm:w-1/2 bg-slate-950 h-3.5 rounded-full overflow-hidden p-0.5 border border-slate-800">
                        <div id="habit-progress-bar" class="bg-gradient-to-r from-neonCyan to-neonGreen h-full w-0 rounded-full transition-all duration-300"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- TAB 4: PSYCHOLOGICAL SUPPORT DIRECTORY -->
        <section id="tab-support" class="tab-content hidden space-y-6">
            <div class="glass-card rounded-2xl p-6 sm:p-8">
                <div class="max-w-2xl mb-6">
                    <span class="px-3 py-1 rounded-full bg-rose-500/10 text-rose-400 text-xs font-semibold border border-rose-500/20 inline-block mb-3">
                        <i class="fa-solid fa-shield-heart mr-1"></i> Hỗ trợ chuyên môn y tế
                    </span>
                    <h2 class="text-xl sm:text-2xl font-bold text-white mb-2 font-tech">Danh Bạ Tư Vấn & Hỗ Trợ Khẩn Cấp</h2>
                    <p class="text-slate-400 text-sm leading-relaxed">
                        Nếu việc chơi game ở mức **Báo động đỏ (Nghiện nặng)** gây suy nhược cơ thể, trầm cảm hoặc xung đột nghiêm trọng, hãy liên hệ các trung tâm tư vấn uy tín tại Việt Nam:
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Unit 1 -->
                    <div class="p-5 rounded-xl bg-slate-950/60 border-l-4 border-l-rose-500 border-y border-r border-slate-800/80 space-y-2">
                        <h3 class="font-bold text-white text-sm sm:text-base">Tổng Đài Quốc Gia Bảo Vệ Trẻ Em & Thanh Thiếu Niên</h3>
                        <p class="text-xs text-slate-400">Tư vấn tâm lý miễn phí 24/7 đối với áp lực học đường, nghiện game & khủng hoảng tâm lý.</p>
                        <div class="pt-2 flex items-center space-x-2 text-rose-400 font-extrabold text-lg">
                            <i class="fa-solid fa-phone"></i>
                            <a href="tel:111" class="hover:underline">111</a>
                        </div>
                    </div>

                    <!-- Unit 2 -->
                    <div class="p-5 rounded-xl bg-slate-950/60 border-l-4 border-l-neonCyan border-y border-r border-slate-800/80 space-y-2">
                        <h3 class="font-bold text-white text-sm sm:text-base">Viện Sức Khỏe Tâm Thần - Bệnh Viện Bạch Mai</h3>
                        <p class="text-xs text-slate-400">Đơn vị y tế chuyên khoa hàng đầu về chẩn đoán và can thiệp rối loạn hành vi nghiện game.</p>
                        <div class="pt-2 flex items-center space-x-2 text-neonCyan font-medium text-xs">
                            <i class="fa-solid fa-location-dot"></i>
                            <span>78 Giải Phóng, Đống Đa, Hà Nội</span>
                        </div>
                    </div>

                    <!-- Unit 3 -->
                    <div class="p-5 rounded-xl bg-slate-950/60 border-l-4 border-l-indigo-500 border-y border-r border-slate-800/80 space-y-2">
                        <h3 class="font-bold text-white text-sm sm:text-base">Bệnh Viện Tâm Thần TP. Hồ Chí Minh</h3>
                        <p class="text-xs text-slate-400">Khám, điều trị y khoa và tư vấn tâm lý chuyên sâu cho thanh thiếu niên và người trưởng thành.</p>
                        <div class="pt-2 flex items-center space-x-2 text-indigo-400 font-medium text-xs">
                            <i class="fa-solid fa-location-dot"></i>
                            <span>760 Hồng Bàng, Phường 1, Quận 11, TP.HCM</span>
                        </div>
                    </div>

                    <!-- Unit 4 -->
                    <div class="p-5 rounded-xl bg-slate-950/60 border-l-4 border-l-amber-500 border-y border-r border-slate-800/80 space-y-2">
                        <h3 class="font-bold text-white text-sm sm:text-base">Lời Khuyên Dành Cho Phụ Huynh & Người Thân</h3>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            Tránh đập phá thiết bị hoặc cắt mạng đột ngột vì có thể kích động hành vi tiêu cực cực đoan. Hãy trò chuyện bình tĩnh, tìm hiểu lý do trốn tránh thực tế và đồng hành cùng chuyên gia.
                        </p>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- MODAL CHIA SẺ KẾT QUẢ ĐA NĂNG -->
    <div id="share-modal" class="fixed inset-0 z-50 hidden bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="glass-card max-w-lg w-full rounded-2xl p-6 space-y-5 border border-cyan-500/30 relative max-h-[90vh] overflow-y-auto">
            
            <!-- Modal Header -->
            <div class="flex justify-between items-center border-b border-slate-800 pb-3">
                <h3 class="text-lg font-extrabold text-white font-tech flex items-center">
                    <i class="fa-solid fa-share-nodes text-neonCyan mr-2.5"></i>
                    CHIA SẺ KẾT QUẢ ĐÁNH GIÁ
                </h3>
                <button onclick="closeShareModal()" class="text-slate-400 hover:text-white p-1 rounded-lg">
                    <i class="fa-solid fa-xmark text-xl"></i>
                </button>
            </div>

            <!-- Native Web Share API Banner -->
            <button onclick="triggerNativeShare()" class="w-full py-3 px-4 rounded-xl bg-gradient-to-r from-neonCyan to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-white font-bold text-sm shadow-glow-cyan flex items-center justify-center space-x-2 transition-all active:scale-95">
                <i class="fa-solid fa-paper-plane"></i>
                <span>Chia Sẻ Nhanh Cho Bạn Bè (Zalo, Messenger...)</span>
            </button>

            <div class="relative flex py-1 items-center">
                <div class="flex-grow border-t border-slate-800"></div>
                <span class="flex-shrink mx-3 text-[11px] text-slate-500 font-bold uppercase">Hoặc chọn phương thức</span>
                <div class="flex-grow border-t border-slate-800"></div>
            </div>

            <!-- Download Result Card Image -->
            <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <div>
                        <h4 class="text-xs font-bold text-slate-200 uppercase">1. Tải Thẻ Kết Quả (Card Image)</h4>
                        <p class="text-[11px] text-slate-400">Tạo file ảnh Cyberpunk kết quả để đăng Story Zalo/FB</p>
                    </div>
                    <button onclick="generateAndDownloadShareCard()" class="px-3.5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition-all flex items-center space-x-1.5 active:scale-95">
                        <i class="fa-solid fa-image"></i>
                        <span>Tải Ảnh PNG</span>
                    </button>
                </div>
            </div>

            <!-- Direct Social Links Grid -->
            <div class="space-y-2">
                <h4 class="text-xs font-bold text-slate-300 uppercase">2. Mạng Xã Hội Direct</h4>
                <div class="grid grid-cols-4 gap-2 text-center">
                    <button onclick="shareSocial('facebook')" class="p-2.5 rounded-xl bg-blue-600/20 border border-blue-500/30 hover:bg-blue-600/40 text-blue-400 transition-all active:scale-95 flex flex-col items-center">
                        <i class="fa-brands fa-facebook text-xl mb-1"></i>
                        <span class="text-[10px] font-semibold">Facebook</span>
                    </button>
                    <button onclick="shareSocial('zalo')" class="p-2.5 rounded-xl bg-cyan-600/20 border border-cyan-500/30 hover:bg-cyan-600/40 text-cyan-400 transition-all active:scale-95 flex flex-col items-center">
                        <i class="fa-solid fa-comment-dots text-xl mb-1"></i>
                        <span class="text-[10px] font-semibold">Zalo</span>
                    </button>
                    <button onclick="shareSocial('telegram')" class="p-2.5 rounded-xl bg-sky-600/20 border border-sky-500/30 hover:bg-sky-600/40 text-sky-400 transition-all active:scale-95 flex flex-col items-center">
                        <i class="fa-brands fa-telegram text-xl mb-1"></i>
                        <span class="text-[10px] font-semibold">Telegram</span>
                    </button>
                    <button onclick="shareSocial('twitter')" class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:bg-slate-700 text-slate-200 transition-all active:scale-95 flex flex-col items-center">
                        <i class="fa-brands fa-x-twitter text-xl mb-1"></i>
                        <span class="text-[10px] font-semibold">Twitter</span>
                    </button>
                </div>
            </div>

            <!-- Copy Link & Text Block -->
            <div class="space-y-2">
                <h4 class="text-xs font-bold text-slate-300 uppercase">3. Sao chép nội dung kết quả</h4>
                <div class="flex space-x-2">
                    <input type="text" id="share-text-input" readonly value="" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-400 focus:outline-none truncate">
                    <button onclick="copyShareText()" class="px-4 py-2 rounded-xl bg-cyan-950 border border-neonCyan/50 hover:bg-neonCyan hover:text-black text-neonCyan font-bold text-xs transition-all flex items-center shrink-0 active:scale-95">
                        <i class="fa-solid fa-copy mr-1.5"></i>
                        <span>Sao chép</span>
                    </button>
                </div>
            </div>

            <!-- QR Code Section -->
            <div class="pt-2 border-t border-slate-800 flex flex-col items-center justify-center space-y-2">
                <span class="text-[11px] font-semibold text-slate-400">4. Quét mã QR để tự mở trên điện thoại khác:</span>
                <div id="qrcode-box" class="p-2.5 bg-white rounded-xl shadow-md"></div>
            </div>

        </div>
    </div>

    <!-- Hidden Canvas used to generate Result Card PNG -->
    <canvas id="shareCanvas" class="hidden" width="800" height="480"></canvas>

    <!-- Footer -->
    <footer class="glass-card border-t border-slate-800/80 py-6 px-4 mt-8 text-center text-xs text-slate-500">
        <div class="max-w-4xl mx-auto space-y-2">
            <p>Bài kiểm tra dựa trên 9 Tiêu chuẩn Chẩn đoán Internet Gaming Disorder (IGD) theo DSM-5 của Hiệp hội Tâm thần học Hoa Kỳ (APA).</p>
            <p>Kết quả mang tính chất tầm soát tâm lý cá nhân, không thay thế hoàn toàn chẩn đoán y khoa lâm sàng trực tiếp từ Bác sĩ.</p>
            <p class="pt-2 text-slate-600 font-tech">© 2026 MindBalance Assessment System. All rights reserved.</p>
        </div>
    </footer>

    <!-- JavaScript Application Core -->
    <script>
        // --- 9 CLINICAL DSM-5 CRITERIA DATA ---
        const dsm5Questions = [
            {
                id: "preoccupation",
                aspect: 4,
                category: "1. Bận tâm quá mức (Preoccupation)",
                text: "Bạn có dành phần lớn thời gian trong ngày suy nghĩ về game ngay cả khi không chơi (ví dụ: nhớ lại trận cũ, thèm chơi, hoặc liên tục lên kế hoạch cho lần chơi tiếp)?"
            },
            {
                id: "withdrawal",
                aspect: 1,
                category: "2. Triệu chứng cai game (Withdrawal)",
                text: "Bạn có cảm thấy bứt rứt, bồn chồn, lo âu, dễ cáu gắt hoặc buồn bã khi bị ép ngừng chơi hoặc không thể kết nối mạng/game?"
            },
            {
                id: "tolerance",
                aspect: 4,
                category: "3. Tăng dung nạp (Tolerance)",
                text: "Bạn có cảm thấy cần phải tăng dần thời gian chơi (chơi lâu hơn) hoặc nạp thêm nhiều tiền/đồ mới tìm lại được cảm giác hưng phấn như trước?"
            },
            {
                id: "control",
                aspect: 4,
                category: "4. Mất khả năng kiểm soát (Loss of Control)",
                text: "Bạn đã từng nhiều lần cố gắng cắt giảm số giờ chơi game hoặc tự hứa bỏ game nhưng đều thất bại?"
            },
            {
                id: "interest",
                aspect: 2,
                category: "5. Bỏ rơi các sở thích khác (Loss of Interests)",
                text: "Bạn có bỏ rơi các thói quen giải trí, môn thể thao yêu thích hoặc giảm các cuộc gặp gỡ bạn bè bên ngoài chỉ để dành trọn thời gian cho game?"
            },
            {
                id: "continued",
                aspect: 3,
                category: "6. Tiếp tục chơi bất chấp hậu quả (Continued Overuse)",
                text: "Bạn có tiếp tục chơi game liên tục dù biết rõ nó đang trực tiếp gây ra hậu quả xấu như thức khuya mệt mỏi, sụt giảm điểm số hoặc trễ deadline công việc?"
            },
            {
                id: "deception",
                aspect: 2,
                category: "7. Nói dối & Che giấu (Deception)",
                text: "Bạn có từng nói dối người thân, gia đình hoặc bạn bè về số giờ thực tế bạn đã tiêu tốn cho việc chơi game?"
            },
            {
                id: "escape",
                aspect: 1,
                category: "8. Giải tỏa cảm xúc tiêu cực (Escape Mood)",
                text: "Bạn có coi game là phương cách chính để trốn tránh thực tế, giải tỏa cảm giác tội lỗi, áp lực cuộc sống, lo âu hay muộn phiền?"
            },
            {
                id: "jeopardy",
                aspect: 3,
                category: "9. Đe dọa mối quan hệ & Sự nghiệp (Jeopardy)",
                text: "Việc chơi game quá độ đã từng làm rạn nứt hoặc nguy cơ làm mất đi một mối quan hệ tình cảm, cơ hội học tập hoặc công việc quan trọng của bạn?"
            }
        ];

        // Binary Options (Yes / No) - SCORES HIDDEN FROM USER
        const optionsData = [
            { text: "CÓ - Đúng với tôi", value: 1, desc: "Xảy ra thường xuyên hoặc gây ảnh hưởng rõ rệt" },
            { text: "KHÔNG - Khác tôi", value: 0, desc: "Không xảy ra hoặc hiếm khi xuất hiện" }
        ];

        const habitsData = [
            "Tắt toàn bộ thông báo ứng dụng game trên điện thoại.",
            "Đặt báo thức đếm ngược tối đa 60 - 90 phút cho mỗi phiên chơi.",
            "Tuyệt đối không để máy tính/điện thoại sát giường ngủ.",
            "Tham gia 1 môn thể thao (Cầu lông, Gym, Chạy bộ) 3 buổi/tuần.",
            "Chỉ mở game sau khi đã hoàn thành toàn bộ bài tập/công việc ngày.",
            "Dành ít nhất 30 phút trò chuyện trực tiếp với gia đình/bạn bè mỗi tối."
        ];

        // --- STATE VARIABLES ---
        let currentIdx = 0;
        let answers = new Array(dsm5Questions.length).fill(null);
        let selectedHabits = new Set();
        let gaugeChartInstance = null;
        let timeChartInstance = null;
        let qrCodeInstance = null;

        // Global result data for share
        let lastResultSummary = {
            score: 0,
            title: "",
            color: "#00f3ff",
            desc: ""
        };

        // --- TAB SWITCHING LOGIC ---
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.nav-btn').forEach(el => {
                el.classList.remove('text-neonCyan', 'bg-slate-800/90');
                el.classList.add('text-slate-400');
            });

            document.getElementById(`tab-${tabId}`).classList.remove('hidden');
            const activeNav = document.getElementById(`nav-${tabId}`);
            if (activeNav) {
                activeNav.classList.add('text-neonCyan', 'bg-slate-800/90');
                activeNav.classList.remove('text-slate-400');
            }

            if (tabId === 'calculator') {
                setTimeout(initTimeChart, 100);
            }
        }

        function toggleMobileMenu() {
            document.getElementById('mobile-menu').classList.toggle('hidden');
        }

        function showToast(msg) {
            const toast = document.getElementById('toast');
            document.getElementById('toast-message').innerText = msg;
            toast.classList.remove('hidden');
            setTimeout(() => {
                toast.classList.add('hidden');
            }, 3000);
        }

        // --- QUIZ STEPPER ENGINE ---
        function startQuiz() {
            document.getElementById('quiz-intro').classList.add('hidden');
            document.getElementById('quiz-container').classList.remove('hidden');
            document.getElementById('quiz-results').classList.add('hidden');
            currentIdx = 0;
            answers.fill(null);
            renderQuestion('next');
        }

        function renderQuestion(direction = 'next') {
            const q = dsm5Questions[currentIdx];
            const qBox = document.getElementById('question-box');

            qBox.classList.remove('question-slide-in', 'question-slide-back');
            void qBox.offsetWidth;
            qBox.classList.add(direction === 'next' ? 'question-slide-in' : 'question-slide-back');

            document.getElementById('question-category').innerText = q.category;
            document.getElementById('question-text').innerText = q.text;
            
            const stepNum = (currentIdx + 1).toString().padStart(2, '0');
            document.getElementById('question-tracker').innerText = `CÂU HỎI ${stepNum} / 09`;
            
            const pct = Math.round(((currentIdx + 1) / dsm5Questions.length) * 100);
            document.getElementById('progress-percent').innerText = `${pct}% Hoàn thành`;
            document.getElementById('progress-bar').style.width = `${pct}%`;

            document.getElementById('btn-prev').disabled = currentIdx === 0;

            const container = document.getElementById('options-container');
            container.innerHTML = '';

            optionsData.forEach((opt) => {
                const isSelected = answers[currentIdx] === opt.value;
                
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = `w-full p-4 rounded-xl border text-left transition-all duration-200 flex items-center justify-between group active:scale-[0.99] ${
                    isSelected 
                        ? 'border-neonCyan bg-cyan-950/40 text-white shadow-glow-cyan option-selected-pulse' 
                        : 'border-slate-800 bg-slate-900/70 text-slate-300 hover:border-slate-600 hover:bg-slate-800/80'
                }`;

                btn.onclick = () => selectOption(opt.value);

                btn.innerHTML = `
                    <div class="flex items-center space-x-3.5">
                        <div class="w-6 h-6 rounded-full border flex items-center justify-center transition-all ${
                            isSelected ? 'border-neonCyan bg-neonCyan text-black' : 'border-slate-600 group-hover:border-slate-400'
                        }">
                            ${isSelected ? '<i class="fa-solid fa-check text-xs check-icon-spin"></i>' : ''}
                        </div>
                        <div>
                            <span class="block font-bold text-sm sm:text-base ${isSelected ? 'text-neonCyan' : 'text-slate-200'}">${opt.text}</span>
                            <span class="block text-xs text-slate-400">${opt.desc}</span>
                        </div>
                    </div>
                `;

                container.appendChild(btn);
            });

            updateNextButtonState();
        }

        function selectOption(val) {
            answers[currentIdx] = val;
            renderQuestion('stay');

            if (currentIdx < dsm5Questions.length - 1) {
                setTimeout(() => {
                    nextQuestion();
                }, 280);
            }
        }

        function updateNextButtonState() {
            const nextBtn = document.getElementById('btn-next');
            const nextText = document.getElementById('btn-next-text');
            const nextIcon = document.getElementById('btn-next-icon');
            
            const hasAnswered = answers[currentIdx] !== null;

            if (currentIdx === dsm5Questions.length - 1) {
                nextText.innerText = "XEM KẾT QUẢ ĐÁNH GIÁ";
                nextIcon.className = "fa-solid fa-chart-line text-xs";
                nextBtn.className = `px-6 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold transition-all flex items-center space-x-2 active:scale-95 ${
                    hasAnswered 
                        ? 'bg-gradient-to-r from-neonCyan to-neonPurple text-white shadow-glow-cyan' 
                        : 'bg-slate-800 text-slate-500 opacity-40 cursor-not-allowed'
                }`;
                nextBtn.disabled = !hasAnswered;
            } else {
                nextText.innerText = "Đi tiếp";
                nextIcon.className = "fa-solid fa-chevron-right text-xs";
                nextBtn.className = `px-6 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all flex items-center space-x-2 active:scale-95 ${
                    hasAnswered 
                        ? 'bg-neonCyan text-black hover:bg-cyan-300 shadow-glow-cyan' 
                        : 'bg-slate-800 text-slate-500 opacity-40 cursor-not-allowed'
                }`;
                nextBtn.disabled = !hasAnswered;
            }
        }

        function nextQuestion() {
            if (answers[currentIdx] === null) return;

            if (currentIdx < dsm5Questions.length - 1) {
                currentIdx++;
                renderQuestion('next');
            } else {
                calculateResults();
            }
        }

        function prevQuestion() {
            if (currentIdx > 0) {
                currentIdx--;
                renderQuestion('back');
            }
        }

        function restartQuiz() {
            startQuiz();
        }

        // --- CALCULATE & DETAILED CLINICAL ANALYSIS ---
        function calculateResults() {
            document.getElementById('quiz-container').classList.add('hidden');
            document.getElementById('quiz-results').classList.remove('hidden');

            const totalScore = answers.reduce((sum, val) => sum + (val || 0), 0);
            document.getElementById('score-number').innerText = totalScore;

            let color = "";
            let title = "";
            let desc = "";
            let recs = [];
            const resultCard = document.getElementById('result-main-card');
            resultCard.classList.remove('severe-alarm-card');

            // 4-LEVEL DSM-5 CLASSIFICATION
            if (totalScore <= 2) {
                color = "#00ff66";
                title = "1. BÌNH THƯỜNG / KIỂM SOÁT TỐT";
                desc = "Bạn thỏa mãn dưới 3 tiêu chuẩn DSM-5. Bạn hoàn toàn giữ được sự chủ động và cân bằng. Việc chơi game của bạn hoàn toàn mang tính chất giải trí lành mạnh.";
                recs = [
                    "🟢 <b>Duy trì phong độ:</b> Tiếp tục giữ kỷ luật bản thân và quản lý thời gian tốt như hiện tại.",
                    "🟢 <b>Đa dạng hóa cuộc sống:</b> Mở rộng thêm các kỹ năng sống, thể thao ngoài trời hoặc ngoại ngữ."
                ];
                triggerConfetti();
            } else if (totalScore <= 4) {
                color = "#f59e0b";
                title = "2. NGUY CƠ NHẸ / CẦN LƯU Ý";
                desc = "Bạn đạt 3-4 tiêu chuẩn DSM-5. Bạn đang xuất hiện một số dấu hiệu mất cân bằng nhỏ. Dù chưa chạm ngưỡng lâm sàng, game đã bắt đầu chiếm dụng thời gian nghỉ ngơi.";
                recs = [
                    "🟡 <b>Đặt giới hạn nghiêm ngặt:</b> Giới hạn chơi game tối đa 1.5 - 2 tiếng/ngày.",
                    "🟡 <b>Không chơi trước khi ngủ:</b> Tắt màn hình trước khi ngủ 1 tiếng để bảo vệ giấc ngủ.",
                    "🟡 <b>Hẹn giờ chủ động:</b> Dùng ứng dụng đếm ngược buộc bản thân đứng dậy khi hết giờ."
                ];
            } else if (totalScore <= 6) {
                color = "#9d00ff";
                title = "3. NGUY CƠ VỪA / NGHIỆN MỨC ĐỘ VỪA";
                desc = "Bạn thỏa mãn 5-6 tiêu chuẩn DSM-5 (đủ ngưỡng chuẩn đoán Internet Gaming Disorder ban đầu). Việc chơi game đã trực tiếp làm gián đoạn học tập/công việc.";
                recs = [
                    "🟣 <b>Thực hiện Digital Detox ngắn hạn:</b> Thách thức bản thân ngưng chơi game trong 3-5 ngày liền.",
                    "🟣 <b>Báo cáo với người thân:</b> Nhờ bạn bè/người thân giám sát và giữ hộ thiết bị trong giờ học/làm việc.",
                    "🟣 <b>Chuyển dịch năng lượng:</b> Thay thế cảm giác thành tựu trong game bằng bài tập gym, chạy bộ."
                ];
            } else {
                color = "#ff0055";
                title = "4. NGHIỆN GAME NẶNG / BÁO ĐỘNG ĐỎ 🚨";
                desc = "Bạn thỏa mãn 7-9/9 tiêu chuẩn DSM-5 lâm sàng. Đây là tình trạng **Nghiện Game Nặng nghiêm trọng**. Game đã chiếm quyền kiểm soát hầu hết cảm xúc, hành vi, gây suy giảm thể chất và mối quan hệ.";
                resultCard.classList.add('severe-alarm-card');
                recs = [
                    "🚨 <b>KẾT NỐI HỖ TRỢ CHUYÊN MÔN NGAY:</b> Đừng ngần ngại tìm kiếm sự trợ giúp từ Bác sĩ tâm lý hoặc Tổng đài 111.",
                    "🚨 <b>Can thiệp hành vi quyết liệt:</b> Xóa ứng dụng game gây nghiện cao, ngắt kết nối mạng sau 22h đêm.",
                    "🚨 <b>Gia đình đồng hành:</b> Cần sự can thiệp và giám sát nhân văn từ cha mẹ/người thân."
                ];
            }

            // Save global state for sharing
            lastResultSummary = {
                score: totalScore,
                title: title,
                color: color,
                desc: desc
            };

            const titleEl = document.getElementById('result-title');
            titleEl.innerText = title;
            titleEl.style.color = color;
            document.getElementById('result-description').innerHTML = desc;

            const recsContainer = document.getElementById('recommendations-content');
            recsContainer.innerHTML = recs.map(r => `<p class="bg-slate-950/80 p-3.5 rounded-xl border border-slate-800/80">${r}</p>`).join('');

            analyze4Aspects();
            renderGaugeChart(totalScore, color);
        }

        // --- DETAILED ANALYSIS OF 4 ASPECTS ---
        function analyze4Aspects() {
            const q2 = answers[1] || 0;
            const q8 = answers[7] || 0;
            const aspect1Score = q2 + q8;
            setAspectUI(1, aspect1Score, 
                aspect1Score === 0 ? "Bình thường" : (aspect1Score === 1 ? "Có dấu hiệu" : "Báo động"),
                aspect1Score === 0 ? "Cảm xúc ổn định, không bị phụ thuộc cảm giác thèm game hay cáu gắt." :
                (aspect1Score === 1 ? "Bắt đầu xuất hiện tâm lý bứt rứt hoặc coi game là nơi trốn tránh áp lực." :
                "Tâm lý phụ thuộc cao, dễ hoảng loạn, cáu gắt mạnh khi bị cấm chơi game.")
            );

            const q5 = answers[4] || 0;
            const q7 = answers[6] || 0;
            const aspect2Score = q5 + q7;
            setAspectUI(2, aspect2Score, 
                aspect2Score === 0 ? "Tốt" : (aspect2Score === 1 ? "Suy giảm nhẹ" : "Tổn thương nặng"),
                aspect2Score === 0 ? "Duy trì tốt tương tác xã hội và sự trung thực với người thân." :
                (aspect2Score === 1 ? "Thỉnh thoảng nói dối về giờ chơi hoặc giảm tương tác ngoài đời." :
                "Nói dối thường xuyên, thu mình, đe dọa làm rạn nứt mối quan hệ gia đình.")
            );

            const q6 = answers[5] || 0;
            const q9 = answers[8] || 0;
            const aspect3Score = q6 + q9;
            setAspectUI(3, aspect3Score, 
                aspect3Score === 0 ? "Đảm bảo" : (aspect3Score === 1 ? "Ảnh hưởng" : "Trì trệ nghiêm trọng"),
                aspect3Score === 0 ? "Hiệu suất học tập và công việc không bị ảnh hưởng bởi game." :
                (aspect3Score === 1 ? "Game làm trễ hạn công việc, khiến cơ thể mệt mỏi vào ban ngày." :
                "Bỏ dở trách nhiệm học tập/làm việc, đối mặt với nguy cơ thất bại hoặc đình chỉ.")
            );

            const q1 = answers[0] || 0;
            const q3 = answers[2] || 0;
            const q4 = answers[3] || 0;
            const aspect4Score = q1 + q3 + q4;
            setAspectUI(4, aspect4Score, 
                aspect4Score === 0 ? "Kiểm soát tốt" : (aspect4Score <= 2 ? "Giảm kiểm soát" : "Mất kiểm soát"),
                aspect4Score === 0 ? "Khả năng làm chủ bản thân tốt, dừng chơi dễ dàng." :
                (aspect4Score <= 2 ? "Dành nhiều suy nghĩ cho game, khó cắt giảm giờ chơi theo ý muốn." :
                "Suy nghĩ luôn bị ám ảnh bởi game, cày cấp vô thức, hoàn toàn mất tự chủ.")
            );
        }

        function setAspectUI(id, score, statusText, descText) {
            const statusEl = document.getElementById(`aspect-status-${id}`);
            const descEl = document.getElementById(`aspect-desc-${id}`);

            statusEl.innerText = statusText;
            descEl.innerText = descText;

            if (score === 0) {
                statusEl.className = "text-xs font-bold px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800";
            } else if (score === 1) {
                statusEl.className = "text-xs font-bold px-2 py-0.5 rounded bg-amber-950 text-amber-400 border border-amber-800";
            } else {
                statusEl.className = "text-xs font-bold px-2 py-0.5 rounded bg-rose-950 text-rose-400 border border-rose-800 animate-pulse";
            }
        }

        // --- MULTI-CHANNEL SHARE HUB SYSTEM ---
        function getShareableText() {
            const pageUrl = window.location.href;
            return `🎯 Mình vừa hoàn thành Bài Đánh Giá Tình Trạng Nghiện Game (DSM-5):\n- Điểm số tiêu chuẩn: ${lastResultSummary.score}/9\n- Mức độ: ${lastResultSummary.title}\n\n👉 Bạn cũng có thể kiểm tra mức độ cân bằng game của mình tại đây: ${pageUrl}`;
        }

        function openShareModal() {
            const shareText = getShareableText();
            document.getElementById('share-text-input').value = shareText;
            document.getElementById('share-modal').classList.remove('hidden');

            // Generate QR Code
            const qrBox = document.getElementById('qrcode-box');
            qrBox.innerHTML = '';
            if (typeof QRCode !== 'undefined') {
                qrCodeInstance = new QRCode(qrBox, {
                    text: window.location.href,
                    width: 100,
                    height: 100,
                    colorDark : "#060913",
                    colorLight : "#ffffff",
                    correctLevel : QRCode.CorrectLevel.H
                });
            }
        }

        function closeShareModal() {
            document.getElementById('share-modal').classList.add('hidden');
        }

        // 1. Native Mobile Web Share API
        async function triggerNativeShare() {
            const shareText = getShareableText();
            if (navigator.share) {
                try {
                    await navigator.share({
                        title: 'Kết Quả Đánh Giá Nghiện Game DSM-5',
                        text: shareText,
                        url: window.location.href,
                    });
                    showToast('Đã chia sẻ thành công!');
                } catch (err) {
                    console.log('User cancelled share', err);
                }
            } else {
                copyShareText();
            }
        }

        // 2. Copy Text & Link to Clipboard
        function copyShareText() {
            const textToCopy = getShareableText();
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(textToCopy).then(() => {
                    showToast('Đã sao chép nội dung & liên kết vào clipboard!');
                }).catch(() => {
                    fallbackCopyText(textToCopy);
                });
            } else {
                fallbackCopyText(textToCopy);
            }
        }

        function fallbackCopyText(text) {
            const input = document.getElementById('share-text-input');
            input.select();
            document.execCommand('copy');
            showToast('Đã sao chép nội dung!');
        }

        // 3. Direct Social Sharing
        function shareSocial(platform) {
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent(`Đánh giá Tình Trạng Nghiện Game DSM-5: Mức độ ${lastResultSummary.title} (${lastResultSummary.score}/9 điểm)`);
            let targetUrl = "";

            if (platform === 'facebook') {
                targetUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
            } else if (platform === 'zalo') {
                targetUrl = `https://sp.zalo.me/share_inline?url=${url}&text=${text}`;
            } else if (platform === 'telegram') {
                targetUrl = `https://t.me/share/url?url=${url}&text=${text}`;
            } else if (platform === 'twitter') {
                targetUrl = `https://twitter.com/intent/tweet?text=${text}&url=${url}`;
            }

            if (targetUrl) {
                window.open(targetUrl, '_blank', 'width=600,height=500');
            }
        }

        // 4. Generate & Download Cyberpunk Card PNG via HTML Canvas
        function generateAndDownloadShareCard() {
            const canvas = document.getElementById('shareCanvas');
            const ctx = canvas.getContext('2d');

            // Background Gradient
            const bgGrad = ctx.createLinearGradient(0, 0, 800, 480);
            bgGrad.addColorStop(0, '#060913');
            bgGrad.addColorStop(0.5, '#0f172a');
            bgGrad.addColorStop(1, '#1e1b4b');
            ctx.fillStyle = bgGrad;
            ctx.fillRect(0, 0, 800, 480);

            // Neon Borders
            ctx.strokeStyle = '#00f3ff';
            ctx.lineWidth = 4;
            ctx.strokeRect(20, 20, 760, 440);

            // Title
            ctx.fillStyle = '#00f3ff';
            ctx.font = 'bold 24px Orbitron, sans-serif';
            ctx.fillText('MIND-BALANCE assessment system', 50, 65);

            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 28px Inter, sans-serif';
            ctx.fillText('KẾT QUẢ ĐÁNH GIÁ NGHIỆN GAME (DSM-5)', 50, 115);

            // Score Box
            ctx.fillStyle = 'rgba(18, 25, 45, 0.9)';
            ctx.fillRect(50, 150, 700, 180);
            ctx.strokeStyle = lastResultSummary.color;
            ctx.lineWidth = 2;
            ctx.strokeRect(50, 150, 700, 180);

            // Score Number
            ctx.fillStyle = lastResultSummary.color;
            ctx.font = 'black 60px Orbitron, sans-serif';
            ctx.fillText(`${lastResultSummary.score}/9`, 80, 235);

            ctx.fillStyle = '#94a3b8';
            ctx.font = '16px Inter, sans-serif';
            ctx.fillText('Tiêu chuẩn chẩn đoán lâm sàng', 80, 275);

            // Result Title
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 22px Inter, sans-serif';
            ctx.fillText(lastResultSummary.title, 260, 210);

            // Description wrap
            ctx.fillStyle = '#cbd5e1';
            ctx.font = '14px Inter, sans-serif';
            const cleanDesc = lastResultSummary.desc.replace(/[*_]/g, '');
            ctx.fillText(cleanDesc.substring(0, 75) + '...', 260, 250);

            // Footer
            ctx.fillStyle = '#64748b';
            ctx.font = '14px Inter, sans-serif';
            ctx.fillText('Quét hoặc truy cập website để tự đánh giá mức độ chơi game của bạn', 50, 400);

            // Download Link
            const link = document.createElement('a');
            link.download = `MindBalance_ShareCard_${Date.now()}.png`;
            link.href = canvas.toDataURL('image/png');
            link.click();
            showToast('Đã tải ảnh Thẻ Kết Quả PNG!');
        }

        // --- CELEBRATION CONFETTI ---
        function triggerConfetti() {
            if (typeof confetti === 'function') {
                confetti({
                    particleCount: 100,
                    spread: 70,
                    origin: { y: 0.6 }
                });
            }
        }

        // --- CHART.JS GAUGE & PIE ---
        function renderGaugeChart(score, colorHex) {
            const ctx = document.getElementById('gaugeChart').getContext('2d');
            
            if (gaugeChartInstance) {
                gaugeChartInstance.destroy();
            }

            gaugeChartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    datasets: [{
                        data: [score, 9 - score],
                        backgroundColor: [colorHex, '#1e293b'],
                        borderWidth: 0,
                    }]
                },
                options: {
                    rotation: -90,
                    circumference: 180,
                    cutout: '78%',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        tooltip: { enabled: false }
                    }
                }
            });
        }

        function initTimeChart() {
            const ctx = document.getElementById('timeDistributionChart').getContext('2d');

            const g = parseFloat(document.getElementById('time-gaming').value) || 0;
            const s = parseFloat(document.getElementById('time-sleep').value) || 0;
            const w = parseFloat(document.getElementById('time-work').value) || 0;
            const o = parseFloat(document.getElementById('time-social').value) || 0;

            const total = g + s + w + o;
            const warningEl = document.getElementById('time-warning');

            if (total > 24) {
                warningEl.classList.remove('hidden');
            } else {
                warningEl.classList.add('hidden');
            }

            const pct = total > 0 ? ((g / 24) * 100).toFixed(1) : 0;
            document.getElementById('gaming-pct-val').innerText = `${pct}% quỹ thời gian 24h`;

            if (timeChartInstance) {
                timeChartInstance.destroy();
            }

            timeChartInstance = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: ['Chơi Game', 'Ngủ & Nghỉ', 'Học / Làm việc', 'Khác & Vận động'],
                    datasets: [{
                        data: [g, s, w, o],
                        backgroundColor: ['#00f3ff', '#6366f1', '#10b981', '#f59e0b'],
                        borderWidth: 2,
                        borderColor: '#060913'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                color: '#94a3b8',
                                font: { size: 10 }
                            }
                        }
                    }
                }
            });
        }

        function updateTimeChart() {
            initTimeChart();
        }

        // --- HABITS PLANNER RENDER ---
        function renderHabits() {
            const container = document.getElementById('habits-list');
            container.innerHTML = '';

            habitsData.forEach((habit, idx) => {
                const isChecked = selectedHabits.has(idx);
                const item = document.createElement('div');
                item.className = `p-4 rounded-xl cursor-pointer border transition-all flex items-start space-x-3.5 ${
                    isChecked ? 'border-neonCyan bg-cyan-950/40' : 'border-slate-800 bg-slate-950/60 hover:border-slate-700'
                }`;
                item.onclick = () => toggleHabit(idx);
                item.innerHTML = `
                    <div class="mt-0.5">
                        ${isChecked 
                            ? '<i class="fa-solid fa-square-check text-neonCyan text-lg"></i>' 
                            : '<i class="fa-regular fa-square text-slate-600 text-lg"></i>'}
                    </div>
                    <span class="text-sm ${isChecked ? 'text-white font-semibold' : 'text-slate-300'}">${habit}</span>
                `;
                container.appendChild(item);
            });

            updateHabitProgress();
        }

        function toggleHabit(idx) {
            if (selectedHabits.has(idx)) {
                selectedHabits.delete(idx);
            } else {
                selectedHabits.add(idx);
            }
            renderHabits();
        }

        function updateHabitProgress() {
            const count = selectedHabits.size;
            const total = habitsData.length;
            const pct = Math.round((count / total) * 100);

            document.getElementById('habit-progress-text').innerText = `Đã chọn ${count} / ${total} mục tiêu`;
            document.getElementById('habit-progress-bar').style.width = `${pct}%`;
        }

        // --- EXPORT REPORT FILE ---
        function downloadResultsReport() {
            const totalScore = answers.reduce((sum, val) => sum + (val || 0), 0);
            let evaluation = "";
            if (totalScore <= 2) evaluation = "1. Bình thường / Kiểm soát tốt";
            else if (totalScore <= 4) evaluation = "2. Nguy cơ nhẹ / Cần lưu ý";
            else if (totalScore <= 6) evaluation = "3. Nguy cơ vừa / Nghiện mức độ vừa";
            else evaluation = "4. NGHIỆN GAME NẶNG / BÁO ĐỘNG ĐỎ 🚨";

            let content = `=================================================\n`;
            content += `BÁO CÁO ĐÁNH GIÁ LÂM SÀNG NGHIỆN GAME (DSM-5)\n`;
            content += `MindBalance System - Ngày tạo: ${new Date().toLocaleDateString('vi-VN')}\n`;
            content += `=================================================\n\n`;
            content += `TỔNG ĐIỂM TIÊU CHUẨN: ${totalScore} / 9 Tiêu chuẩn\n`;
            content += `PHÂN LOẠI MỨC ĐỘ: ${evaluation}\n\n`;
            content += `CHI TIẾT 9 CÂU HỎI TIÊU CHUẨN LÂM SÀNG:\n`;
            
            dsm5Questions.forEach((q, i) => {
                const ansText = answers[i] === 1 ? "CÓ" : "KHÔNG";
                content += `${i + 1}. ${q.category}: [${ansText}]\n`;
            });

            content += `\n-------------------------------------------------\n`;
            content += `Ghi chú: Kết quả dùng cho mục đích tầm soát cá nhân theo DSM-5 (APA).`;

            const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `MindBalance_DSM5_Report_${Date.now()}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        // --- INIT ON LOAD ---
        window.onload = function() {
            renderHabits();
        };
    </script>
</body>
</html>