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
        .font-tech { font-family: 'Orbitron', sans-serif; }
        .glass-card {
            background: rgba(18, 25, 45, 0.75);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        @keyframes slideInRight {
            from { opacity: 0; transform: translateX(30px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .question-slide-in { animation: slideInRight 0.35s ease-out forwards; }
        @keyframes pulseGlow {
            0% { box-shadow: 0 0 0 0 rgba(0, 243, 255, 0.4); }
            70% { box-shadow: 0 0 0 12px rgba(0, 243, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 243, 255, 0); }
        }
        .option-selected-pulse { animation: pulseGlow 0.6s ease-out; }
        @keyframes checkSpin {
            0% { transform: scale(0) rotate(-90deg); opacity: 0; }
            100% { transform: scale(1) rotate(0deg); opacity: 1; }
        }
        .check-icon-spin { animation: checkSpin 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
        @keyframes alarmPulse {
            0%, 100% { border-color: rgba(255, 0, 85, 0.8); box-shadow: 0 0 15px rgba(255, 0, 85, 0.4); }
            50% { border-color: rgba(255, 0, 85, 0.3); box-shadow: 0 0 35px rgba(255, 0, 85, 0.7); }
        }
        .severe-alarm-card { animation: alarmPulse 2s infinite ease-in-out; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #060913; }
        ::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #00f3ff; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-neonCyan selection:text-black">

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 hidden bg-slate-900 border border-neonCyan text-white px-5 py-3 rounded-xl shadow-glow-cyan flex items-center space-x-3">
        <i class="fa-solid fa-circle-check text-neonCyan text-lg"></i>
        <span id="toast-message" class="text-xs sm:text-sm font-semibold">Đã sao chép liên kết vào bộ nhớ tạm!</span>
    </div>

    <!-- Header Navigation -->
    <header class="sticky top-0 z-40 glass-card border-b border-slate-800/80 px-4 lg:px-8 py-3">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
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

            <nav class="hidden md:flex space-x-1 bg-slate-950/80 p-1 rounded-xl border border-slate-800">
                <button onclick="switchTab('assessment')" id="nav-assessment" class="px-4 py-2 rounded-lg text-xs font-semibold text-neonCyan bg-slate-800/90 transition-all flex items-center">
                    <i class="fa-solid fa-clipboard-check mr-2"></i>Đánh giá DSM-5
                </button>
                <button onclick="switchTab('calculator')" id="nav-calculator" class="px-4 py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-slate-200 transition-all flex items-center">
                    <i class="fa-solid fa-chart-pie mr-2"></i>Phân bổ thời gian
                </button>
                <button onclick="switchTab('planner')" id="nav-planner" class="px-4 py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-slate-200 transition-all flex items-center">
                    <i class="fa-solid fa-bullseye mr-2"></i>Mục tiêu & Thói quen
                </button>
                <button onclick="switchTab('support')" id="nav-support" class="px-4 py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-slate-200 transition-all flex items-center">
                    <i class="fa-solid fa-heart-pulse mr-2 text-rose-500"></i>Hỗ trợ tâm lý
                </button>
            </nav>

            <button onclick="toggleMobileMenu()" class="md:hidden text-slate-300 hover:text-white p-2 rounded-lg bg-slate-900 border border-slate-800">
                <i class="fa-solid fa-bars text-lg"></i>
            </button>
        </div>

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

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 py-6 sm:py-10 w-full flex-grow">

        <!-- TAB 1: ASSESSMENT QUIZ -->
        <section id="tab-assessment" class="tab-content space-y-6">
            
            <!-- Intro Banner -->
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
                    Bài trắc nghiệm gồm <b class="text-neonCyan">9 tiêu chí lâm sàng chuẩn quốc tế</b>. Trong quá trình làm bài, điểm số được ẩn hoàn toàn để đảm bảo tính khách quan. Bản phân tích chi tiết mức độ (Bình thường, Nguy cơ nhẹ, Vừa, Nghiện nặng) sẽ hiển thị ngay sau khi hoàn thành.
                </p>

                <div class="flex flex-wrap gap-4 items-center">
                    <button onclick="startQuiz()" class="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-gradient-to-r from-cyan-500 via-indigo-600 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white font-bold text-sm tracking-wide shadow-glow-cyan transition-all transform active:scale-95 flex items-center justify-center space-x-2">
                        <span>BẮT ĐẦU ĐÁNH GIÁ</span>
                        <i class="fa-solid fa-arrow-right text-xs"></i>
                    </button>
                    <span class="text-xs text-slate-400 flex items-center justify-center w-full sm:w-auto">
                        <i class="fa-solid fa-shield-halved mr-1.5 text-neonCyan"></i> Bảo mật tuyệt đối • Đồng bộ thiết bị
                    </span>
                </div>
            </div>

            <!-- Quiz Stepper Wizard Container -->
            <div id="quiz-container" class="hidden glass-card rounded-2xl p-5 sm:p-8 space-y-6">
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-xs font-semibold">
                        <span id="question-tracker" class="text-slate-300 font-tech">CÂU HỎI 01 / 09</span>
                        <span id="progress-percent" class="text-neonCyan font-bold">11% Hoàn thành</span>
                    </div>
                    <div class="w-full h-3 bg-slate-900 rounded-full overflow-hidden p-0.5 border border-slate-800">
                        <div id="progress-bar" class="h-full bg-gradient-to-r from-neonCyan via-indigo-500 to-neonPurple rounded-full transition-all duration-300 w-[11%]"></div>
                    </div>
                </div>

                <div id="question-box" class="py-2">
                    <span id="question-category" class="inline-block text-[11px] font-bold uppercase tracking-widest text-neonCyan px-2.5 py-1 rounded-md bg-cyan-950/60 border border-cyan-800/50 mb-3">
                        --
                    </span>
                    <h3 id="question-text" class="text-lg sm:text-2xl font-bold text-white leading-relaxed">
                        --
                    </h3>
                </div>

                <div class="grid grid-cols-1 gap-3.5" id="options-container">
                    <!-- Options injected dynamically without showing points -->
                </div>

                <div class="flex items-center justify-between pt-5 border-t border-slate-800/80">
                    <button id="btn-prev" onclick="prevQuestion()" disabled class="px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 text-xs sm:text-sm font-semibold transition-all disabled:opacity-30 disabled:cursor-not-allowed flex items-center space-x-2">
                        <i class="fa-solid fa-chevron-left text-xs"></i>
                        <span>Quay lại</span>
                    </button>

                    <div class="text-xs text-slate-500 hidden sm:block italic">
                        Chọn đáp án phản ánh đúng thực tế của bạn
                    </div>

                    <button id="btn-next" onclick="nextQuestion()" disabled class="px-6 py-2.5 rounded-xl bg-slate-800 text-slate-500 text-xs sm:text-sm font-bold transition-all disabled:opacity-40 disabled:cursor-not-allowed flex items-center space-x-2">
                        <span id="btn-next-text">Đi tiếp</span>
                        <i id="btn-next-icon" class="fa-solid fa-chevron-right text-xs"></i>
                    </button>
                </div>
            </div>

            <!-- Quiz Results View -->
            <div id="quiz-results" class="hidden space-y-6">
                <div id="result-main-card" class="glass-card rounded-2xl p-6 sm:p-10 text-center relative overflow-hidden">
                    <div class="inline-block px-3 py-1 rounded-full bg-slate-900 border border-slate-800 text-xs font-semibold text-slate-400 mb-2">
                        KẾT QUẢ ĐÁNH GIÁ LÂM SÀNG DSM-5
                    </div>

                    <h2 id="result-title" class="text-2xl sm:text-4xl font-extrabold mb-2 font-tech">--</h2>

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

                    <div class="flex flex-wrap justify-center gap-3">
                        <button onclick="restartQuiz()" class="px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 text-xs sm:text-sm font-semibold transition-all flex items-center space-x-2">
                            <i class="fa-solid fa-rotate-left"></i>
                            <span>Làm Lại</span>
                        </button>
                        <button onclick="openShareModal()" class="px-6 py-2.5 rounded-xl bg-gradient-to-r from-neonCyan via-indigo-600 to-neonPurple text-white text-xs sm:text-sm font-extrabold shadow-glow-cyan transition-all flex items-center space-x-2">
                            <i class="fa-solid fa-share-nodes text-base"></i>
                            <span>CHIA SẺ KẾT QUẢ</span>
                        </button>
                        <button onclick="downloadResultsReport()" class="px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 text-xs sm:text-sm font-semibold transition-all flex items-center space-x-2">
                            <i class="fa-solid fa-download"></i>
                            <span>Tải Báo Cáo (.txt)</span>
                        </button>
                    </div>
                </div>

                <!-- 4 Detailed Aspects Analysis -->
                <div class="glass-card rounded-2xl p-6 sm:p-8 space-y-4">
                    <h3 class="text-lg font-bold text-white flex items-center border-b border-slate-800 pb-3">
                        <i class="fa-solid fa-chart-bar text-neonCyan mr-2.5 text-xl"></i>
                        Phân Tích Chi Tiết 4 Khía Cạnh Cuộc Sống
                    </h3>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
                        <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold uppercase tracking-wide text-cyan-400"><i class="fa-solid fa-brain mr-2"></i>1. Tâm Thần & Cảm Xúc</span>
                                <span id="aspect-status-1" class="text-xs font-bold px-2 py-0.5 rounded bg-slate-900">--</span>
                            </div>
                            <p id="aspect-desc-1" class="text-xs text-slate-300 leading-relaxed">--</p>
                        </div>
                        <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold uppercase tracking-wide text-purple-400"><i class="fa-solid fa-users mr-2"></i>2. Mối Quan Hệ Xã Hội</span>
                                <span id="aspect-status-2" class="text-xs font-bold px-2 py-0.5 rounded bg-slate-900">--</span>
                            </div>
                            <p id="aspect-desc-2" class="text-xs text-slate-300 leading-relaxed">--</p>
                        </div>
                        <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold uppercase tracking-wide text-emerald-400"><i class="fa-solid fa-briefcase mr-2"></i>3. Học Tập & Công Việc</span>
                                <span id="aspect-status-3" class="text-xs font-bold px-2 py-0.5 rounded bg-slate-900">--</span>
                            </div>
                            <p id="aspect-desc-3" class="text-xs text-slate-300 leading-relaxed">--</p>
                        </div>
                        <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800/80 space-y-2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold uppercase tracking-wide text-amber-400"><i class="fa-solid fa-sliders mr-2"></i>4. Khả Năng Tự Kiểm Soát</span>
                                <span id="aspect-status-4" class="text-xs font-bold px-2 py-0.5 rounded bg-slate-900">--</span>
                            </div>
                            <p id="aspect-desc-4" class="text-xs text-slate-300 leading-relaxed">--</p>
                        </div>
                    </div>
                </div>

                <!-- Recommendations -->
                <div class="glass-card rounded-2xl p-6 sm:p-8 space-y-4">
                    <h3 class="text-lg font-bold text-white flex items-center">
                        <i class="fa-solid fa-compass text-amber-400 mr-2.5 text-xl"></i>
                        Chiến Lược Can Thiệp Chuyên Suyên
                    </h3>
                    <div id="recommendations-content" class="space-y-3 text-sm text-slate-300"></div>
                </div>
            </div>
        </section>

        <!-- TAB 2: TIME CALCULATOR -->
        <section id="tab-calculator" class="tab-content hidden space-y-6">
            <div class="glass-card rounded-2xl p-6 sm:p-8">
                <h2 class="text-xl sm:text-2xl font-bold text-white mb-2 font-tech">Bảng Tính Quỹ Thời Gian Trong Ngày</h2>
                <p class="text-slate-400 text-sm mb-6">Nhập số giờ trung bình cho từng hoạt động (tổng 24h) để theo dõi tỷ lệ phân bổ.</p>
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                    <div class="lg:col-span-6 space-y-4">
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-neonCyan mb-1.5">🎮 Chơi Game (Giờ/ngày)</label>
                            <input type="number" id="time-gaming" value="4" min="0" max="24" step="0.5" oninput="updateTimeChart()" class="w-full bg-slate-950 border border-slate-700 focus:border-neonCyan rounded-xl px-4 py-3 text-white focus:outline-none font-semibold">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-indigo-400 mb-1.5">😴 Ngủ & Nghỉ ngơi (Giờ/ngày)</label>
                            <input type="number" id="time-sleep" value="7" min="0" max="24" step="0.5" oninput="updateTimeChart()" class="w-full bg-slate-950 border border-slate-700 focus:border-indigo-500 rounded-xl px-4 py-3 text-white focus:outline-none font-semibold">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-emerald-400 mb-1.5">📚 Học tập / Làm việc (Giờ/ngày)</label>
                            <input type="number" id="time-work" value="7" min="0" max="24" step="0.5" oninput="updateTimeChart()" class="w-full bg-slate-950 border border-slate-700 focus:border-emerald-500 rounded-xl px-4 py-3 text-white focus:outline-none font-semibold">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-amber-400 mb-1.5">⚽ Thể thao, Bạn bè & Khác (Giờ/ngày)</label>
                            <input type="number" id="time-social" value="2" min="0" max="24" step="0.5" oninput="updateTimeChart()" class="w-full bg-slate-950 border border-slate-700 focus:border-amber-500 rounded-xl px-4 py-3 text-white focus:outline-none font-semibold">
                        </div>
                        <div id="time-warning" class="hidden p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs font-medium">
                            <i class="fa-solid fa-triangle-exclamation mr-1"></i> Tổng thời gian vượt quá 24h!
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

        <!-- TAB 3: PLANNER -->
        <section id="tab-planner" class="tab-content hidden space-y-6">
            <div class="glass-card rounded-2xl p-6 sm:p-8">
                <h2 class="text-xl sm:text-2xl font-bold text-white mb-2 font-tech">Xây Dựng Thói Quen Kiểm Soát Game</h2>
                <p class="text-slate-400 text-sm mb-6">Đánh dấu những hành động cam kết thực hiện từ hôm nay:</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5" id="habits-list"></div>
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

        <!-- TAB 4: SUPPORT -->
        <section id="tab-support" class="tab-content hidden space-y-6">
            <div class="glass-card rounded-2xl p-6 sm:p-8">
                <div class="max-w-2xl mb-6">
                    <span class="px-3 py-1 rounded-full bg-rose-500/10 text-rose-400 text-xs font-semibold border border-rose-500/20 inline-block mb-3">
                        <i class="fa-solid fa-shield-heart mr-1"></i> Hỗ trợ chuyên môn y tế
                    </span>
                    <h2 class="text-xl sm:text-2xl font-bold text-white mb-2 font-tech">Danh Bạ Tư Vấn & Hỗ Trợ Khẩn Cấp</h2>
                    <p class="text-slate-400 text-sm leading-relaxed">
                        Nếu tình trạng nghiện game ở mức báo động đỏ gây ảnh hưởng nghiêm trọng đến sức khỏe và tâm lý, hãy liên hệ các cơ quan chuyên môn uy tín tại Việt Nam:
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-5 rounded-xl bg-slate-950/60 border-l-4 border-l-rose-500 border-y border-r border-slate-800/80 space-y-2">
                        <h3 class="font-bold text-white text-sm sm:text-base">Tổng Đài Quốc Gia Bảo Vệ Trẻ Em & Thanh Thiếu Niên</h3>
                        <p class="text-xs text-slate-400">Tư vấn tâm lý miễn phí 24/7 đối với áp lực học đường & nghiện game.</p>
                        <div class="pt-2 flex items-center space-x-2 text-rose-400 font-extrabold text-lg">
                            <i class="fa-solid fa-phone"></i>
                            <a href="tel:111" class="hover:underline">111</a>
                        </div>
                    </div>
                    <div class="p-5 rounded-xl bg-slate-950/60 border-l-4 border-l-neonCyan border-y border-r border-slate-800/80 space-y-2">
                        <h3 class="font-bold text-white text-sm sm:text-base">Viện Sức Khỏe Tâm Thần - Bệnh Viện Bạch Mai</h3>
                        <p class="text-xs text-slate-400">Đơn vị y tế chuyên khoa hàng đầu về chẩn đoán và điều trị rối loạn hành vi.</p>
                        <div class="pt-2 flex items-center space-x-2 text-neonCyan font-medium text-xs">
                            <i class="fa-solid fa-location-dot"></i>
                            <span>78 Giải Phóng, Đống Đa, Hà Nội</span>
                        </div>
                    </div>
                    <div class="p-5 rounded-xl bg-slate-950/60 border-l-4 border-l-indigo-500 border-y border-r border-slate-800/80 space-y-2">
                        <h3 class="font-bold text-white text-sm sm:text-base">Bệnh Viện Tâm Thần TP. Hồ Chí Minh</h3>
                        <p class="text-xs text-slate-400">Khám, điều trị y khoa và tư vấn tâm lý chuyên sâu.</p>
                        <div class="pt-2 flex items-center space-x-2 text-indigo-400 font-medium text-xs">
                            <i class="fa-solid fa-location-dot"></i>
                            <span>760 Hồng Bàng, Phường 1, Quận 11, TP.HCM</span>
                        </div>
                    </div>
                    <div class="p-5 rounded-xl bg-slate-950/60 border-l-4 border-l-amber-500 border-y border-r border-slate-800/80 space-y-2">
                        <h3 class="font-bold text-white text-sm sm:text-base">Lời Khuyên Cho Phụ Huynh & Người Thân</h3>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            Tránh la mắng hoặc cấm đoán đột ngột gây phản ứng phòng vệ. Hãy đồng hành, lắng nghe và thiết lập thời gian biểu khoa học cùng người chơi.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- SHARE MODAL -->
    <div id="share-modal" class="fixed inset-0 z-50 hidden bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="glass-card rounded-2xl max-w-md w-full p-6 space-y-6 relative border border-slate-700 animate-toast">
            <button onclick="closeShareModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
            <div class="text-center space-y-2">
                <div class="w-12 h-12 rounded-full bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center mx-auto text-neonCyan">
                    <i class="fa-solid fa-share-nodes text-xl"></i>
                </div>
                <h3 class="text-lg font-bold text-white font-tech">Chia Sẻ Kết Quả Đánh Giá</h3>
                <p class="text-xs text-slate-400">Lan tỏa nhận thức sức khỏe tâm thần đến bạn bè và người thân</p>
            </div>

            <div class="space-y-3">
                <button onclick="shareNative()" class="w-full py-3 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-white text-xs font-bold flex items-center justify-center space-x-2 transition-all">
                    <i class="fa-solid fa-paper-plane text-neonCyan"></i>
                    <span>Chia sẻ qua Zalo, Messenger, SMS...</span>
                </button>
                <button onclick="copyShareLink()" class="w-full py-3 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-white text-xs font-bold flex items-center justify-center space-x-2 transition-all">
                    <i class="fa-solid fa-copy text-indigo-400"></i>
                    <span>Sao chép Liên kết & Nội dung</span>
                </button>
            </div>

            <div class="p-4 bg-slate-950/80 rounded-xl border border-slate-800 flex flex-col items-center justify-center space-y-2">
                <span class="text-[11px] text-slate-400 font-semibold">Quét mã QR để làm bài test trên điện thoại:</span>
                <div id="qrcode" class="p-2 bg-white rounded-lg"></div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="glass-card border-t border-slate-800/80 py-6 text-center text-xs text-slate-500 mt-12">
        <p>MIND-BALANCE © 2026 • Hệ thống tầm soát sức khỏe số dựa trên tiêu chuẩn DSM-5</p>
    </footer>

    <!-- JavaScript Application Logic -->
    <script>
        // 9 DSM-5 Internet Gaming Disorder Criteria (Points hidden during test)
        const questions = [
            { category: "1. Bận tâm quá mức", text: "Bạn có thường xuyên nghĩ về trò chơi ngay cả khi đang làm việc, học tập hoặc không chơi không?" },
            { category: "2. Triệu chứng cai nghiện", text: "Bạn có cảm thấy bứt rứt, cáu gắt, lo âu hoặc buồn bã khi không được chơi game không?" },
            { category: "3. Tính dung nạp", text: "Bạn có cảm giác ngày càng cần phải dành nhiều thời gian hơn hoặc chơi các tựa game mạnh hơn để đạt được sự thỏa mãn không?" },
            { category: "4. Mất kiểm soát", text: "Bạn đã nhiều lần cố gắng giảm thời gian chơi hoặc bỏ game nhưng không thành công?" },
            { category: "5. Mất hứng thú", text: "Bạn có bỏ bê các sở thích cũ, hoạt động ngoài trời hoặc tụ tập bạn bè vì dành toàn bộ thời gian cho game không?" },
            { category: "6. Tiếp tục chơi dù biết hậu quả", text: "Bạn vẫn tiếp tục chơi game với thời lượng lớn dù đã nhận thức rõ các tác động tiêu cực đến sức khỏe, học tập hoặc công việc?" },
            { category: "7. Nói dối", text: "Bạn có từng che giấu gia đình, bạn bè hoặc thầy cô về số thời gian thực tế mình đã bỏ ra để chơi game không?" },
            { category: "8. Trốn tránh cảm xúc", text: "Bạn có dùng game như một công cụ chính để chạy trốn khỏi tâm trạng tồi tệ, căng thẳng hoặc lo âu trong cuộc sống thực?" },
            { category: "9. Nguy cơ mất quan hệ / công việc", text: "Bạn đã từng mạo hiểm hoặc đánh mất các mối quan hệ quan trọng, cơ hội học tập hoặc thăng tiến vì game chưa?" }
        ];

        let currentQuestion = 0;
        let userAnswers = new Array(questions.length).fill(null);
        let gaugeChartInstance = null;
        let timeChartInstance = null;

        const habitsData = [
            { title: "Đặt giờ giới nghiêm kỹ thuật số", desc: "Tắt toàn bộ thiết bị và game trước khi đi ngủ 1 tiếng." },
            { title: "Giới hạn khung giờ chơi cố định", desc: "Chỉ cho phép bản thân chơi tối đa 1-2 khung giờ đã định trước trong ngày." },
            { title: "Tham gia vận động thể thao", desc: "Dành ít nhất 30 phút mỗi ngày chạy bộ, gym hoặc chơi thể thao ngoài trời." },
            { title: "Mở rộng tương tác trực tiếp", desc: "Hẹn gặp bạn bè hoặc gia đình ăn uống, trò chuyện trực tiếp thay vì qua màn hình." },
            { title: "Thay thế bằng kỹ năng mới", desc: "Học đàn, đọc sách, nấu ăn hoặc làm đồ thủ công khi cơn thèm game xuất hiện." },
            { title: "Xóa bớt game gây nghiện nặng", desc: "Gỡ cài đặt các tựa game có tính chất cày cuốc hoặc cuốn hút thời gian mạnh." }
        ];

        // Switch Tabs
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.getElementById(`tab-${tabId}`).classList.remove('hidden');

            document.querySelectorAll('nav button').forEach(btn => {
                btn.classList.remove('text-neonCyan', 'bg-slate-800/90');
                btn.classList.add('text-slate-400');
            });
            const activeBtn = document.getElementById(`nav-${tabId}`);
            if(activeBtn) {
                activeBtn.classList.add('text-neonCyan', 'bg-slate-800/90');
                activeBtn.classList.remove('text-slate-400');
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function toggleMobileMenu() {
            const menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden');
        }

        function startQuiz() {
            document.getElementById('quiz-intro').classList.add('hidden');
            document.getElementById('quiz-container').classList.remove('hidden');
            currentQuestion = 0;
            renderQuestion();
        }

        function renderQuestion() {
            const q = questions[currentQuestion];
            document.getElementById('question-tracker').innerText = `CÂU HỎI ${String(currentQuestion + 1).padStart(2, '0')} / 09`;
            const pct = Math.round(((currentQuestion + 1) / questions.length) * 100);
            document.getElementById('progress-percent').innerText = `${pct}% Hoàn thành`;
            document.getElementById('progress-bar').style.width = `${pct}%`;

            document.getElementById('question-category').innerText = q.category;
            document.getElementById('question-text').innerText = q.text;

            const optionsContainer = document.getElementById('options-container');
            optionsContainer.innerHTML = '';

            const options = [
                { label: "Có / Thường xuyên / Đúng với tôi", val: 1 },
                { label: "Không / Hiếm khi / Không đúng", val: 0 }
            ];

            options.forEach(opt => {
                const isSelected = userAnswers[currentQuestion] === opt.val;
                const btn = document.createElement('button');
                btn.className = `w-full p-4 rounded-xl text-left font-medium text-xs sm:text-sm transition-all flex items-center justify-between border ${
                    isSelected 
                        ? 'bg-cyan-950/80 border-neonCyan text-white shadow-glow-cyan option-selected-pulse' 
                        : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-600 hover:bg-slate-900/80'
                }`;
                
                btn.innerHTML = `
                    <div class="flex items-center space-x-3">
                        <div class="w-5 h-5 rounded-full border ${isSelected ? 'border-neonCyan bg-neonCyan text-black flex items-center justify-center font-bold' : 'border-slate-600'}">
                            ${isSelected ? '<i class="fa-solid fa-check text-xs check-icon-spin"></i>' : ''}
                        </div>
                        <span>${opt.label}</span>
                    </div>
                `;

                btn.onclick = () => selectOption(opt.val, btn);
                optionsContainer.appendChild(btn);
            });

            document.getElementById('btn-prev').disabled = currentQuestion === 0;
            const nextBtn = document.getElementById('btn-next');
            if (userAnswers[currentQuestion] !== null) {
                nextBtn.disabled = false;
                nextBtn.classList.remove('bg-slate-800', 'text-slate-500');
                nextBtn.classList.add('bg-gradient-to-r', 'from-cyan-500', 'to-indigo-600', 'text-white', 'shadow-glow-cyan');
            } else {
                nextBtn.disabled = true;
                nextBtn.classList.add('bg-slate-800', 'text-slate-500');
                nextBtn.classList.remove('bg-gradient-to-r', 'from-cyan-500', 'to-indigo-600', 'text-white', 'shadow-glow-cyan');
            }

            const nextText = document.getElementById('btn-next-text');
            const nextIcon = document.getElementById('btn-next-icon');
            if (currentQuestion === questions.length - 1) {
                nextText.innerText = "Xem Kết Quả Chi Tiết";
                nextIcon.className = "fa-solid fa-flag-checkered text-xs";
            } else {
                nextText.innerText = "Đi tiếp";
                nextIcon.className = "fa-solid fa-chevron-right text-xs";
            }
        }

        function selectOption(val, btnElement) {
            userAnswers[currentQuestion] = val;
            renderQuestion();
        }

        function nextQuestion() {
            if (userAnswers[currentQuestion] === null) return;
            if (currentQuestion < questions.length - 1) {
                currentQuestion++;
                renderQuestion();
            } else {
                calculateResult();
            }
        }

        function prevQuestion() {
            if (currentQuestion > 0) {
                currentQuestion--;
                renderQuestion();
            }
        }

        function calculateResult() {
            document.getElementById('quiz-container').classList.add('hidden');
            const resultDiv = document.getElementById('quiz-results');
            resultDiv.classList.remove('hidden');

            const totalScore = userAnswers.reduce((a, b) => a + (b || 0), 0);
            document.getElementById('score-number').innerText = totalScore;

            let title = "", desc = "", levelColor = "", cardClass = "";

            if (totalScore <= 2) {
                title = "MỨC 1: BÌNH THƯỜNG & KIỂM SOÁT TỐT";
                desc = "Bạn duy trì cân bằng tuyệt vời giữa thế giới ảo và đời thực. Game chỉ đóng vai trò là công cụ giải trí lành mạnh.";
                levelColor = "#00ff66";
            } else if (totalScore <= 4) {
                title = "MỨC 2: NGUY CƠ NHẸ / CẦN LƯU Ý";
                desc = "Bạn có xu hướng dành nhiều thời gian hơn dự kiến cho game. Hãy chủ động thiết lập lại thời gian biểu để tránh trượt dài.";
                levelColor = "#f59e0b";
            } else if (totalScore <= 6) {
                title = "MỨC 3: NGHIỆN GAME MỨC ĐỘ VỪA";
                desc = "Thói quen chơi game bắt đầu ảnh hưởng đến học tập, công việc và các mối quan hệ xã hội của bạn. Cần có kế hoạch điều chỉnh nghiêm túc.";
                levelColor = "#ff0055";
            } else {
                title = "MỨC 4: NGHIỆN GAME NẶNG / BÁO ĐỘNG ĐỎ";
                desc = "Hành vi chơi game đã vượt ngoài tầm kiểm soát, thỏa mãn tiêu chuẩn lâm sàng DSM-5 nghiêm trọng. Cần can thiệp hành vi khẩn cấp hoặc hỗ trợ y tế chuyên khoa.";
                levelColor = "#ff0000";
                cardClass = "severe-alarm-card";
            }

            document.getElementById('result-title').innerText = title;
            document.getElementById('result-title').style.color = levelColor;
            document.getElementById('result-description').innerText = desc;
            
            const mainCard = document.getElementById('result-main-card');
            mainCard.className = `glass-card rounded-2xl p-6 sm:p-10 text-center relative overflow-hidden ${cardClass}`;

            renderGaugeChart(totalScore);
            renderAspectsAnalysis(totalScore);
            renderRecommendations(totalScore);

            confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } });
        }

        function renderGaugeChart(score) {
            const ctx = document.getElementById('gaugeChart').getContext('2d');
            if (gaugeChartInstance) gaugeChartInstance.destroy();

            gaugeChartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    datasets: [{
                        data: [score, 9 - score],
                        backgroundColor: [
                            score <= 2 ? '#00ff66' : score <= 4 ? '#f59e0b' : score <= 6 ? '#ff0055' : '#ff0000',
                            '#1e293b'
                        ],
                        borderWidth: 0
                    }]
                },
                options: {
                    rotation: -90,
                    circumference: 180,
                    cutout: '75%',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { tooltip: { enabled: false }, legend: { display: false } }
                }
            });
        }

        function renderAspectsAnalysis(score) {
            const aspects = [
                {
                    status: score <= 2 ? "Ổn định" : score <= 5 ? "Căng thẳng" : "Kiệt quệ tâm thần",
                    desc: score <= 2 ? "Tâm trạng thoải mái, không bị chi phối bởi các cảm giác tội lỗi hay bứt rứt." : "Thường xuyên có cảm giác lo âu, bứt rứt khi không được cầm máy."
                },
                {
                    status: score <= 2 ? "Gắn kết tốt" : score <= 5 ? "Xa cách" : "Đứt gãy quan hệ",
                    desc: score <= 2 ? "Duy trì tương tác hòa hợp với gia đình và bạn bè ngoài đời thực." : "Giảm thời gian giao tiếp thực tế, dễ xảy ra mâu thuẫn với người thân."
                },
                {
                    status: score <= 2 ? "Hiệu suất cao" : score <= 5 ? "Sao nhãng" : "Sa sút nghiêm trọng",
                    desc: score <= 2 ? "Hoàn thành tốt các mục tiêu học tập, công việc đúng thời hạn." : "Hay buồn ngủ, thiếu tập trung, kết quả học tập hoặc công việc suy giảm."
                },
                {
                    status: score <= 2 ? "Làm chủ tốt" : score <= 5 ? "Dễ sa đà" : "Mất tự chủ hoàn toàn",
                    desc: score <= 2 ? "Biết dừng đúng lúc khi có việc quan trọng hơn." : "Khó kháng cự lại sự cám dỗ của trò chơi, thường xuyên thức khuya."
                }
            ];

            aspects.forEach((asp, i) => {
                document.getElementById(`aspect-status-${i+1}`).innerText = asp.status;
                document.getElementById(`aspect-desc-${i+1}`).innerText = asp.desc;
            });
        }

        function renderRecommendations(score) {
            const container = document.getElementById('recommendations-content');
            let html = '';
            if (score <= 2) {
                html = `
                    <div class="flex items-start space-x-3 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                        <i class="fa-solid fa-circle-check text-emerald-400 mt-1"></i>
                        <div><strong class="text-white">Duy trì lối sống hiện tại:</strong> Tiếp tục cân bằng giữa học tập, giải trí và thể thao để giữ gìn sức khỏe thể chất lẫn tinh thần.</div>
                    </div>
                `;
            } else if (score <= 5) {
                html = `
                    <div class="flex items-start space-x-3 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                        <i class="fa-solid fa-triangle-exclamation text-amber-400 mt-1"></i>
                        <div><strong class="text-white">Thiết lập giới hạn thời gian (Digital Detox):</strong> Cố định khung giờ chơi game không quá 2 giờ/ngày và tuyệt đối không chơi sau 10 giờ đêm.</div>
                    </div>
                    <div class="flex items-start space-x-3 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                        <i class="fa-solid fa-person-running text-cyan-400 mt-1"></i>
                        <div><strong class="text-white">Đổi mới hoạt động ngoại khóa:</strong> Tham gia các câu lạc bộ thể thao hoặc hoạt động ngoài trời để lấp đầy thời gian trống.</div>
                    </div>
                `;
            } else {
                html = `
                    <div class="flex items-start space-x-3 p-3 rounded-xl bg-rose-500/10 border border-rose-500/30">
                        <i class="fa-solid fa-triangle-exclamation text-rose-500 mt-1"></i>
                        <div><strong class="text-white">Can thiệp khẩn cấp & Đồng hành cùng gia đình:</strong> Cần sự hỗ trợ trực tiếp từ gia đình để cắt giảm thiết bị điện tử từng bước một.</div>
                    </div>
                    <div class="flex items-start space-x-3 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                        <i class="fa-solid fa-hospital text-neonCyan mt-1"></i>
                        <div><strong class="text-white">Tìm kiếm chuyên gia tâm lý:</strong> Nên đến các bệnh viện chuyên khoa tâm thần hoặc trung tâm tư vấn tâm lý uy tín để được hỗ trợ liệu pháp hành vi nhận thức (CBT).</div>
                    </div>
                `;
            }
            container.innerHTML = html;
        }

        function restartQuiz() {
            document.getElementById('quiz-results').classList.add('hidden');
            document.getElementById('quiz-intro').classList.remove('hidden');
            userAnswers = new Array(questions.length).fill(null);
        }

        function downloadResultsReport() {
            const score = userAnswers.reduce((a, b) => a + (b || 0), 0);
            const content = `--- BÁO CÁO ĐÁNH GIÁ TÌNH TRẠNG NGHIỆN GAME (DSM-5) ---\nĐiểm số tổng: ${score} / 9 tiêu chuẩn.\nThời gian: ${new Date().toLocaleString()}\n--------------------------------------------------\nMIND-BALANCE SYSTEM`;
            const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'Bao_Cao_Danh_Gia_Nghien_Game.txt';
            a.click();
        }

        // Time Calculator & Chart
        function initTimeChart() {
            const ctx = document.getElementById('timeDistributionChart').getContext('2d');
            timeChartInstance = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: ['Chơi game', 'Ngủ', 'Học/Làm việc', 'Thể thao/Khác'],
                    datasets: [{
                        data: [4, 7, 7, 2],
                        backgroundColor: ['#00f3ff', '#6366f1', '#10b981', '#f59e0b'],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 10 } } } }
                }
            });
            updateTimeChart();
        }

        function updateTimeChart() {
            const gaming = parseFloat(document.getElementById('time-gaming').value) || 0;
            const sleep = parseFloat(document.getElementById('time-sleep').value) || 0;
            const work = parseFloat(document.getElementById('time-work').value) || 0;
            const social = parseFloat(document.getElementById('time-social').value) || 0;
            const total = gaming + sleep + work + social;

            const warning = document.getElementById('time-warning');
            if (total > 24) warning.classList.remove('hidden');
            else warning.classList.add('hidden');

            const gamingPct = ((gaming / 24) * 100).toFixed(1);
            document.getElementById('gaming-pct-val').innerText = `${gamingPct}% cuộc sống`;

            if (timeChartInstance) {
                timeChartInstance.data.datasets[0].data = [gaming, sleep, work, social];
                timeChartInstance.update();
            }
        }

        // Habits Planner
        function initHabits() {
            const container = document.getElementById('habits-list');
            container.innerHTML = '';
            habitsData.forEach((h, idx) => {
                const div = document.createElement('div');
                div.className = "p-4 rounded-xl bg-slate-950/60 border border-slate-800 flex items-start space-x-3 cursor-pointer hover:border-slate-700 transition-all";
                div.innerHTML = `
                    <input type="checkbox" id="habit-${idx}" onchange="updateHabitProgress()" class="mt-1 w-4 h-4 rounded accent-cyan-400 cursor-pointer">
                    <div>
                        <label for="habit-${idx}" class="font-bold text-white text-xs sm:text-sm cursor-pointer">${h.title}</label>
                        <p class="text-xs text-slate-400 mt-0.5">${h.desc}</p>
                    </div>
                `;
                container.appendChild(div);
            });
        }

        function updateHabitProgress() {
            let checkedCount = 0;
            habitsData.forEach((_, idx) => {
                if (document.getElementById(`habit-${idx}`).checked) checkedCount++;
            });
            const pct = Math.round((checkedCount / habitsData.length) * 100);
            document.getElementById('habit-progress-text').innerText = `Đã chọn ${checkedCount} / ${habitsData.length} mục tiêu`;
            document.getElementById('habit-progress-bar').style.width = `${pct}%`;
        }

        // Share Modal
        function openShareModal() {
            document.getElementById('share-modal').classList.remove('hidden');
            const qrContainer = document.getElementById('qrcode');
            qrContainer.innerHTML = '';
            new QRCode(qrContainer, {
                text: window.location.href,
                width: 120,
                height: 120,
                colorDark: "#000000",
                colorLight: "#ffffff",
                correctLevel: QRCode.CorrectLevel.H
            });
        }

        function closeShareModal() {
            document.getElementById('share-modal').classList.add('hidden');
        }

        function shareNative() {
            if (navigator.share) {
                navigator.share({
                    title: 'Đánh Giá Nghiện Game DSM-5',
                    text: 'Hãy thử làm bài đánh giá tình trạng chơi game theo tiêu chuẩn y khoa ngay hôm nay!',
                    url: window.location.href,
                }).catch(console.error);
            } else {
                copyShareLink();
            }
        }

        function copyShareLink() {
            navigator.clipboard.writeText(window.location.href);
            showToast('Đã sao chép liên kết bài test vào bộ nhớ tạm!');
            closeShareModal();
        }

        function showToast(msg) {
            const toast = document.getElementById('toast');
            document.getElementById('toast-message').innerText = msg;
            toast.classList.remove('hidden');
            setTimeout(() => toast.classList.add('hidden'), 3000);
        }

        // Initialize on load
        window.onload = () => {
            initTimeChart();
            initHabits();
        };
    </script>
</body>
</html>
