self.waveform_plot = PlotWidget(self.central_widget)
self.waveform_plot.setMinimumHeight(100)
self.waveform_plot.setBackground(QColor("#1c1c1c"))
self.waveform_plot.showGrid(x=True, y=True, alpha=0.3)
self.layout.addWidget(self.waveform_plot)

self.effects_layout = QHBoxLayout()
self.layout.addLayout(self.effects_layout)

self.reverb_button = QPushButton("Reverb", self.central_widget)
self.effects_layout.addWidget(self.reverb_button)
self.reverb_button.clicked.connect(self.reverb)

self.compressor_button = QPushButton("Compressor", self.central_widget)
self.effects_layout.addWidget(self.compressor_button)
self.compressor_button.clicked.connect(self.compress)

self.delay_button = QPushButton("Delay", self.central_widget)
self.effects_layout.addWidget(self.delay_button)
self.delay_button.clicked.connect(self.delay)

self.distortion_button = QPushButton("Distortion", self.central_widget)
self.effects_layout.addWidget(self.distortion_button)
self.distortion_button.clicked.connect(self.distortion)

self.gain_button = QPushButton("Gain", self.central_widget)
self.effects_layout.addWidget(self.gain_button)
self.gain_button.clicked.connect(self.gain)

self.highpass_button = QPushButton("Highpass", self.central_widget)
self.effects_layout.addWidget(self.highpass_button)
self.highpass_button.clicked.connect(self.high_pass)

self.lowpass_button = QPushButton("Lowpass", self.central_widget)
self.effects_layout.addWidget(self.lowpass_button)
self.lowpass_button.clicked.connect(self.low_pass)

self.apply_effects_button = QPushButton("Apply Effects", self.central_widget)
self.apply_effects_button.setStyleSheet("background-color: #F0F0F0; color: #1c1c1c;")
self.effects_layout.addWidget(self.apply_effects_button)
self.apply_effects_button.clicked.connect(self.apply_effects)

self.board = Pedalboard()
self.playing_state = False
self.add_menu()

self.timer = QTimer(self)
self.timer.setInterval(100)  # Update waveform every 100 milliseconds
self.timer.timeout.connect(self.update_waveform)