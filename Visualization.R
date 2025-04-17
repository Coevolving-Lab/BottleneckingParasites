library(ggplot2)
library(dplyr)
library(tidyr)

#Set the working directory for the "project" folder here:
setwd("[Put Actual Path Here]/project")

####Figure 1 - Recurring bottlenecks with three values for bottleneck frequency####
figure_1_max_prev_data <- read.csv(file = "./output/figure_1_max_prev_data.csv", header = TRUE)
figure_1_prev_range_data <- read.csv(file = "./output/figure_1_prev_range_data.csv", header = TRUE)

PlottingDF_2_Max_Prev <- figure_1_max_prev_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 2) %>%
  filter(InitialPrevalence == 1.0) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

PlottingDF_2_Prev_Range <- figure_1_prev_range_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 2) %>%
  filter(InitialPrevalence != 1.0) %>%
  group_by(InitialPrevalence) %>%
  mutate(GlobalTime = (row_number() / ScalingFactor) + 2.01) %>% #Gets this range aligned with the first bottleneck
  mutate(Prevalence = I / (S + I + R))

tiff("./Figures/Figure 1/2 Panel.tiff", units="in", width = 20, height = 4, res=300)
ggplot(data = PlottingDF_2_Max_Prev, aes(x = GlobalTime, y = Prevalence)) +
  ylim(0, 1) +
  xlim(0, 30) +
  geom_vline(xintercept = 2.01, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 4.02, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 6.03, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 8.04, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 10.05, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 12.06, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 14.07, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 16.08, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 18.09, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 20.10, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 22.11, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 24.12, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 26.13, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 28.14, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_line(data = PlottingDF_2_Prev_Range, 
            aes(x = GlobalTime,
                y = Prevalence, 
                group = InitialPrevalence),
            color = "dark grey",
            linewidth = 0.75) +
  geom_line(linewidth = 1.5) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  theme_minimal() +
  theme(axis.text.x = element_blank(),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()


PlottingDF_3_Max_Prev <- figure_1_max_prev_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 3) %>%
  filter(InitialPrevalence == 1.0) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

PlottingDF_3_Prev_Range <- figure_1_prev_range_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 3) %>%
  filter(InitialPrevalence != 1.0) %>%
  group_by(InitialPrevalence) %>%
  mutate(GlobalTime = (row_number() / ScalingFactor) + 3.01) %>% #Gets this range aligned with the first bottleneck
  mutate(Prevalence = I / (S + I + R))

tiff("./Figures/Figure 1/3 Panel.tiff", units="in", width = 20, height = 4, res=300)
ggplot(data = PlottingDF_3_Max_Prev, aes(x = GlobalTime, y = Prevalence)) +
  ylim(0, 1) +
  xlim(1, 31) +
  geom_vline(xintercept = 3.01, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 6.02, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 9.03, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 12.04, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 15.05, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 18.06, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 21.07, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 24.08, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 27.09, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_line(data = PlottingDF_3_Prev_Range, 
            aes(x = GlobalTime,
                y = Prevalence, 
                group = InitialPrevalence),
            color = "dark grey",
            linewidth = 0.75) +
  geom_line(linewidth = 1.5) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  theme_minimal() +
  theme(axis.text.x = element_blank(),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()

PlottingDF_4_Max_Prev <- figure_1_max_prev_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 4) %>%
  filter(InitialPrevalence == 1.0) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

PlottingDF_4_Prev_Range <- figure_1_prev_range_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 4) %>%
  filter(InitialPrevalence != 1.0) %>%
  group_by(InitialPrevalence) %>%
  mutate(GlobalTime = (row_number() / ScalingFactor) + 4.01) %>% #Gets this range aligned with the first bottleneck
  mutate(Prevalence = I / (S + I + R))

tiff("./Figures/Figure 1/4 Panel.tiff", units="in", width = 20, height = 4, res=300)
ggplot(data = PlottingDF_4_Max_Prev, aes(x = GlobalTime, y = Prevalence)) +
  ylim(0, 1) +
  xlim(2, 32) +
  geom_vline(xintercept = 4.01, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 8.02, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 12.03, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 16.04, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 20.05, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 24.06, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_vline(xintercept = 28.07, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_line(data = PlottingDF_4_Prev_Range, 
            aes(x = GlobalTime,
                y = Prevalence, 
                group = InitialPrevalence),
            color = "dark grey",
            linewidth = 0.75) +
  geom_line(linewidth = 1.5) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  theme_minimal() +
  theme(axis.text.x = element_blank(),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()

#Empty panels
PanelDF <- figure_1_max_prev_data %>%
  mutate(Time = row_number(),
         Prevalence = I  / (S + I + R))

tiff("./Figures/Figure 1/Empty Panels.tiff", units="in", width = 18, height = 12, res=300)
ggplot(data = PanelDF, aes(x = Time, y = Prevalence)) +
  facet_grid(TimeTillBottleneckMean~.) +
  theme_minimal() +
  theme(axis.text.x = element_blank(),
        strip.text = element_blank(),
        axis.title.x = element_text(size = 36, face = "bold"),
        axis.text.y = element_text(size = 24),
        axis.title.y = element_text(size = 36, face = "bold"),
        panel.border = element_rect(color = "black", linewidth = 2),
        panel.spacing = unit(2, "lines"))
dev.off()


####Figure 2 - pmax and pmin across range of bottleneck frequency####
figure_2_data <- read.csv(file = "./output/figure_2_data.csv", header = TRUE)

PlottingDF <- figure_2_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(ScaledTimeTillBottleneckMean) %>%
  summarize(PMax = max(Prevalence),
            PMin = min(Prevalence))

tiff("./Figures/Figure 2/Figure 2 Unlabeled.tiff", units="in", width = 6, height = 5, res=300)
ggplot(data = PlottingDF) +
  ylim(0, 1) +
  geom_ribbon(aes(x = ScaledTimeTillBottleneckMean, ymin = PMin, ymax = PMax), fill = "red", alpha = 0.25) +
  geom_line(aes(x = ScaledTimeTillBottleneckMean, y = PMax), linewidth = 1, linetype = "dashed") +
  geom_line(aes(x = ScaledTimeTillBottleneckMean, y = PMin), linewidth = 1, linetype = "dashed") +
  xlab("Timesteps Between Bottlenecks") +
  ylab("Parasite Prevalence") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()

####Figure 3 - Examples of parasite extinction####
figure_3_deterministic_data <- read.csv(file = "./output/figure_3_deterministic_data.csv", header = TRUE)
figure_3_stochastic_data <- read.csv(file = "./output/figure_3_stochastic_data.csv", header = TRUE)


#2 Timesteps
PlottingDF2Deterministic <- figure_3_deterministic_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 2) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

PlottingDF2Stochastic <- figure_3_stochastic_data %>%
  select(Rep, Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(Rep, ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 2) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(Rep) %>%
  mutate(GlobalTime = row_number() / ScalingFactor)

ExtinctionTimeDF2 <- PlottingDF2Stochastic %>%
  filter(Prevalence == 0) %>%
  group_by(Rep) %>%
  summarize(ExtinctionTime = first(GlobalTime))

tiff("./Figures/Figure 3/2 Panel.tiff", units="in", width = 20, height = 4, res=300)
ggplot() +
  ylim(0, 1) +
  xlim(0, 100) +
  geom_line(data = PlottingDF2Stochastic, 
            aes(x = GlobalTime, y = Prevalence, group = Rep), 
            color = "dark grey",
            linewidth = 0.75) +
  geom_line(data = PlottingDF2Deterministic, 
            aes(x = GlobalTime, y = Prevalence),
            linewidth = 1.5) +
  geom_point(data = ExtinctionTimeDF2, aes(x = ExtinctionTime, y = 0), color = "dark red", size = 3)+
  xlab("Time") +
  ylab("Parasite Prevalence") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()

#3 Timesteps
PlottingDF3Deterministic <- figure_3_deterministic_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 3) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

PlottingDF3Stochastic <- figure_3_stochastic_data %>%
  select(Rep, Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(Rep, ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 3) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(Rep) %>%
  mutate(GlobalTime = row_number() / ScalingFactor)

ExtinctionTimeDF3 <- PlottingDF3Stochastic %>%
  filter(Prevalence == 0) %>%
  group_by(Rep) %>%
  summarize(ExtinctionTime = first(GlobalTime))

tiff("./Figures/Figure 3/3 Panel.tiff", units="in", width = 20, height = 4, res=300)
ggplot() +
  ylim(0, 1) +
  xlim(0, 100) +
  geom_line(data = PlottingDF3Stochastic, 
            aes(x = GlobalTime - 1, y = Prevalence, group = Rep), 
            color = "dark grey",
            linewidth = 0.75) +
  geom_line(data = PlottingDF3Deterministic, 
            aes(x = GlobalTime - 1, y = Prevalence),
            linewidth = 1.5) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()

#4 Timesteps
PlottingDF4Deterministic <- figure_3_deterministic_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 4) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

PlottingDF4Stochastic <- figure_3_stochastic_data %>%
  select(Rep, Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(Rep, ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  filter(ScaledTimeTillBottleneckMean == 4) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(Rep) %>%
  mutate(GlobalTime = row_number() / ScalingFactor)

ExtinctionTimeDF4 <- PlottingDF4Stochastic %>%
  filter(Prevalence == 0) %>%
  group_by(Rep) %>%
  summarize(ExtinctionTime = first(GlobalTime))

tiff("./Figures/Figure 3/4 Panel.tiff", units="in", width = 20, height = 4, res=300)
ggplot() +
  ylim(0, 1) +
  xlim(0, 100) +
  geom_line(data = PlottingDF4Stochastic, 
            aes(x = GlobalTime - 2, y = Prevalence, group = Rep), 
            color = "dark grey",
            linewidth = 0.75) +
  geom_line(data = PlottingDF4Deterministic, 
            aes(x = GlobalTime - 2, y = Prevalence),
            linewidth = 1.5) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()

#Empty Panels
PanelDF <- figure_3_deterministic_data %>%
  mutate(Time = row_number(),
         Prevalence = I  / (S + I + R))

tiff("./Figures/Figure 3/Empty Panels.tiff", units="in", width = 18, height = 12, res=300)
ggplot(data = PanelDF, aes(x = Time, y = Prevalence)) +
  facet_grid(TimeTillBottleneckMean~.) +
  theme_minimal() +
  theme(axis.text.x = element_blank(),
        strip.text = element_blank(),
        axis.title.x = element_text(size = 36, face = "bold"),
        axis.text.y = element_text(size = 24),
        axis.title.y = element_text(size = 36, face = "bold"),
        panel.border = element_rect(color = "black", linewidth = 2),
        panel.spacing = unit(2, "lines"))
dev.off()


####Figure 4 - Extinction versus variation in bottleneck frequency####
figure_4_data <- read.csv(file = "./output/figure_4_data.csv", header = TRUE)

PlottingDF <- figure_4_data %>%
  select(Rep, Timepoint, S, I, R, TimeTillBottleneckMean, TimeTillBottleneckCV, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(Rep, ScaledTimepoint, S, I, R, ScaledTimeTillBottleneckMean, TimeTillBottleneckCV, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(ScaledTimeTillBottleneckMean, TimeTillBottleneckCV, Rep) %>%
  summarize(ExtinctionOccurred = case_when(min(Prevalence) == 0~TRUE,
                                           min(Prevalence) > 0~FALSE)) %>%
  mutate(TotalReps = max(Rep) + 1) %>% #Since "Rep" starts with 0
  group_by(ScaledTimeTillBottleneckMean, TimeTillBottleneckCV, TotalReps) %>%
  summarize(ExtinctionCount = sum(ExtinctionOccurred == TRUE)) %>%
  mutate(ExtinctionProbability = ExtinctionCount / TotalReps)

#Since the full data is very large, I have included a saved copy of "PlottingDF", the summarized
#data, in the Figures/Figure 4 folder that can be loaded directly
PlottingDF <- read.csv(file = "./Figures/Figure 4/figure_4_summarized_data.csv", header = TRUE)

tiff("./Figures/Figure 4/Figure 4.tiff", units="in", width = 8, height = 5, res=300)
ggplot(data = PlottingDF, aes(x = ScaledTimeTillBottleneckMean, y = ExtinctionProbability, 
                              group = TimeTillBottleneckCV, color = TimeTillBottleneckCV)) +
  geom_line(linewidth = 1) +
  scale_color_gradient(low = "black", high = "light grey") +
  labs(color = "Coefficient of\nVariation") +
  xlab("Timesteps Between Bottlenecks (Mean)") +
  ylab("Parasite Extinction Probability") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 12),
        legend.title = element_text(size = 14, face = "bold"))
dev.off()


####Figure 5 - Extinction versus variation in bottleneck severity####
figure_5_data <- read.csv(file = "./output/figure_5_data.csv", header = TRUE)

PlottingDF <- figure_5_data %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(BottleneckSizeMean, BottleneckSizeCV, CarryingCapacity, Rep) %>%
  summarize(ExtinctionOccurred = case_when(min(Prevalence) == 0~TRUE,
                                           min(Prevalence) > 0~FALSE)) %>%
  mutate(TotalReps = max(Rep) + 1) %>% #Since "Rep" starts with 0
  group_by(BottleneckSizeMean, BottleneckSizeCV, CarryingCapacity, TotalReps) %>%
  summarize(ExtinctionCount = sum(ExtinctionOccurred == TRUE)) %>%
  mutate(ExtinctionProbability = ExtinctionCount / TotalReps) %>%
  mutate(BottleneckSizeOutOfK = BottleneckSizeMean / CarryingCapacity)

#Since the full data is very large, I have included a saved copy of "PlottingDF", the summarized
#data, in the Figures/Figure 5 folder that can be loaded directly
PlottingDF <- read.csv(file = "./Figures/Figure 5/figure_5_summarized_data.csv", header = TRUE)

tiff("./Figures/Figure 5/Figure 5.tiff", units="in", width = 8, height = 5, res=300)
ggplot(data = PlottingDF, aes(x = BottleneckSizeOutOfK, y = ExtinctionProbability, 
                              group = BottleneckSizeCV, color = BottleneckSizeCV)) +
  geom_line(linewidth = 1) +
  scale_color_gradient(low = "black", high = "light grey") +
  labs(color = "Coefficient of\nVariation") +
  xlab("Mean Bottleneck Severity\n(Proportion of Carrying Capacity Surviving)") +
  ylab("Parasite Extinction Probability") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()


####Figure S1 - examples of population size dynamics#####
figure_s1_data <- read.csv(file = "./output/figure_s1_data.csv", header = TRUE)

PlottingDF <- figure_s1_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BottleneckSizeMean, CarryingCapacity, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  mutate(BottleneckSizeOutOfK = BottleneckSizeMean / CarryingCapacity) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, BottleneckSizeMean, BottleneckSizeOutOfK, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  group_by(ScaledTimeTillBottleneckMean, BottleneckSizeMean, BottleneckSizeOutOfK) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  mutate(BottleneckFrequencyLabel = ScaledTimeTillBottleneckMean)

BottleneckTimeDF <- PlottingDF %>%
  filter(round(S + I + R) == BottleneckSizeMean)


tiff("./Figures/Figure S1/Figure S1 Unlabeled.tiff", units="in", width = 8, height = 5, res=300)
ggplot() +
  facet_grid(ScaledTimeTillBottleneckMean~BottleneckSizeOutOfK) +
  scale_x_continuous(limits = c(-1, 8), breaks = c(0, 2, 4, 6, 8)) +
  ylim(0, 1000) +
  geom_vline(data = BottleneckTimeDF,
             aes(xintercept = GlobalTime - ScaledTimeTillBottleneckMean),
             linetype = "dashed", 
             color = "dark grey", 
             linewidth = 1) +
  geom_ribbon(data = PlottingDF, 
              aes(x = GlobalTime - ScaledTimeTillBottleneckMean, ymin = 0, ymax = S+I+R),
              fill = "grey",
              alpha = 0.25) +
  geom_line(data = PlottingDF,
            aes(x = GlobalTime - ScaledTimeTillBottleneckMean, y = S+I+R),
            linewidth = 1.0) +
  xlab("Time") +
  ylab("Total Population Size") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        panel.border = element_rect(linewidth = 1, fill = NA),
        strip.text.x = element_text(size = 20),
        strip.text.y = element_text(size = 20))
dev.off()


####Figure S2 - Examples of models with different birth and transmission functions####
df1 = read.csv(file = "./output/figure_s2_regulated_ddt_data.csv", header = TRUE)
df2 = read.csv(file = "./output/figure_s2_exponential_ddt_data.csv", header = TRUE)
df3 = read.csv(file = "./output/figure_s2_regulated_fdt_data.csv", header = TRUE)
df4 = read.csv(file = "./output/figure_s2_exponential_fdt_data.csv", header = TRUE)

combined_dataframe = rbind(df1, df2, df3, df4)

PlottingDF <- combined_dataframe %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate, BirthType, TransmissionType) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor, BirthType, TransmissionType) %>%
  group_by(BirthType, TransmissionType) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  filter(GlobalTime > 4)

PlottingDF$BirthType <- as.factor(PlottingDF$BirthType)
PlottingDF$BirthType <- recode_factor(PlottingDF$BirthType, 
                                      Regulated = "Regulated\nBirth", 
                                      Exponential = "Exponential\nBirth")
PlottingDF$TransmissionType <- as.factor(PlottingDF$TransmissionType)
PlottingDF$TransmissionType <- recode_factor(PlottingDF$TransmissionType, 
                                             Density = "Density-\nDependent\nTransmission", 
                                             Frequency = "Frequency-\nDependent\nTransmission")

tiff("./Figures/Figure S2/Figure S2.tiff", units="in", width = 8, height = 5, res=300)
ggplot(data = PlottingDF, aes(x = GlobalTime - 6, y = Prevalence)) +
  facet_grid(TransmissionType~BirthType) +
  ylim(0, 1) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_line(linewidth = 1.5) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        panel.border = element_rect(linewidth = 1, fill = NA),
        strip.text.x = element_text(size = 20),
        strip.text.y = element_text(size = 20))
dev.off()


####Figure S3 - Recovery Rate Range figure####
single_bottleneck_data <- read.csv(file = "./output/figure_s3_single_bottleneck_data.csv", header = TRUE)

SinglePlottingDF <- single_bottleneck_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate, RecoveryRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledRecoveryRate = RecoveryRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScaledRecoveryRate, ScalingFactor) %>%
  group_by(ScaledRecoveryRate) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

tiff("./Figures/Figure S3/Figure S3 Single Bottleneck Panel.tiff", units="in", width = 8, height = 5, res=300)
ggplot(data = SinglePlottingDF, aes(x = GlobalTime, y = Prevalence, group = ScaledRecoveryRate, color  = ScaledRecoveryRate)) +
  ylim(0, 1) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_line(linewidth = 1) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  labs(color = "Recovery Rate") +
  scale_color_gradient(low = "black", high = "#f5d142") +
  theme_minimal() +
  theme(axis.text.x = element_blank(),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()


recurring_bottleneck_data <- read.csv(file = "./output/figure_s3_recurring_bottleneck_data.csv", header = TRUE)

RecurringPlottingDF <- recurring_bottleneck_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate, RecoveryRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledRecoveryRate = RecoveryRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScaledRecoveryRate, ScalingFactor) %>%
  group_by(ScaledRecoveryRate) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

tiff("./Figures/Figure S3/Figure S3 Recurring Bottleneck Panel.tiff", units="in", width = 15, height = 4, res=300)
ggplot(data = RecurringPlottingDF, aes(x = GlobalTime, y = Prevalence, group = ScaledRecoveryRate, color = ScaledRecoveryRate)) +
  ylim(0, 1) +
  xlim(0, 30) +
  geom_vline(xintercept = 3.01, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 6.02, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 9.03, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 12.04, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 15.05, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 18.06, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 21.07, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 24.08, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 27.09, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_line(linewidth = 1) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  labs(color = "Recovery Rate") +
  scale_color_gradient(low = "black", high = "#f5d142") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()


recurring_bottleneck_data <- read.csv(file = "./output/figure_s3_recurring_bottleneck_data.csv", header = TRUE)

SIRDF <- recurring_bottleneck_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate, RecoveryRate) %>%
  filter(RecoveryRate == 0.001) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledRecoveryRate = RecoveryRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScaledRecoveryRate, ScalingFactor) %>%
  group_by(ScaledRecoveryRate) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(N = S + I + R) %>%
  mutate(SFrequency = S / N,
         IFrequency = I / N,
         RFrequency = R / N)
  

tiff("./Figures/Figure S3/Figure S3 SIR Panel.tiff", units="in", width = 15, height = 4, res=300)
ggplot(data = SIRDF, aes(x = GlobalTime)) +
  ylim(0, 1) +
  xlim(0, 30) +
  geom_ribbon(aes(ymin = 0, 
                  ymax = IFrequency), 
              fill = "black") +
  geom_ribbon(aes(ymin = IFrequency, 
                  ymax = IFrequency + RFrequency), 
              fill = "darkgrey") +
  geom_ribbon(aes(ymin = IFrequency + RFrequency, 
                  ymax = 1),
              fill = "grey98") +
  geom_vline(xintercept = 3.01, linetype = "dashed", color = "red", linewidth = 0.75) +
  geom_vline(xintercept = 6.02, linetype = "dashed", color = "red", linewidth = 0.75) +
  geom_vline(xintercept = 9.03, linetype = "dashed", color = "red", linewidth = 0.75) +
  geom_vline(xintercept = 12.04, linetype = "dashed", color = "red", linewidth = 0.75) +
  geom_vline(xintercept = 15.05, linetype = "dashed", color = "red", linewidth = 0.75) +
  geom_vline(xintercept = 18.06, linetype = "dashed", color = "red", linewidth = 0.75) +
  geom_vline(xintercept = 21.07, linetype = "dashed", color = "red", linewidth = 0.75) +
  geom_vline(xintercept = 24.08, linetype = "dashed", color = "red", linewidth = 0.75) +
  geom_vline(xintercept = 27.09, linetype = "dashed", color = "red", linewidth = 0.75) +
  xlab("Time") +
  ylab("Host Class Frequency") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()

####Figure S4 - Infected Death Rate Range figure####
single_bottleneck_data <- read.csv(file = "./output/figure_s4_single_bottleneck_data.csv", header = TRUE)

SinglePlottingDF <- single_bottleneck_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate, IDeathRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledIDeathRate = IDeathRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScaledIDeathRate, ScalingFactor) %>%
  group_by(ScaledIDeathRate) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))
  
tiff("./Figures/Figure S4/Figure S4 Single Bottleneck Panel.tiff", units="in", width = 8, height = 5, res=300)
ggplot(data = SinglePlottingDF, aes(x = GlobalTime, y = Prevalence, group = ScaledIDeathRate, color  = ScaledIDeathRate)) +
  ylim(0, 1) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "dark grey", linewidth = 1) +
  geom_line(linewidth = 1) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  labs(color = "Infected Death Rate") +
  scale_color_gradient(low = "black", high = "purple") +
  theme_minimal() +
  theme(axis.text.x = element_blank(),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()


recurring_bottleneck_data <- read.csv(file = "./output/figure_s4_recurring_bottleneck_data.csv", header = TRUE)

RecurringPlottingDF <- recurring_bottleneck_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate, IDeathRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledIDeathRate = IDeathRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScaledIDeathRate, ScalingFactor) %>%
  group_by(ScaledIDeathRate) %>%
  mutate(GlobalTime = row_number() / ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R))

tiff("./Figures/Figure S4/Figure S4 Recurring Bottleneck Panel.tiff", units="in", width = 15, height = 4, res=300)
ggplot(data = RecurringPlottingDF, aes(x = GlobalTime, y = Prevalence, group = ScaledIDeathRate, color = ScaledIDeathRate)) +
  ylim(0, 1) +
  xlim(0, 30) +
  geom_vline(xintercept = 3.01, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 6.02, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 9.03, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 12.04, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 15.05, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 18.06, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 21.07, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 24.08, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_vline(xintercept = 27.09, linetype = "dashed", color = "dark grey", linewidth = 0.75) +
  geom_line(linewidth = 1) +
  xlab("Time") +
  ylab("Parasite Prevalence") +
  labs(color = "Infected Death Rate") +
  scale_color_gradient(low = "black", high = "purple") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()


####Figure S5 - pmax and pmin across a range of bottleneck frequency (across transmission rates)#####

figure_s5_000125_data <- read.csv(file = "./output/figure_s5_00125_data.csv", header = TRUE)
figure_s5_0025_data <- read.csv(file = "./output/figure_s5_0025_data.csv", header = TRUE)
figure_s5_005_data <- read.csv(file = "./output/figure_s5_005_data.csv", header = TRUE)
figure_s5_01_data <- read.csv(file = "./output/figure_s5_01_data.csv", header = TRUE)

figure_s5_data <- rbind(figure_s5_000125_data, figure_s5_0025_data, figure_s5_005_data, figure_s5_01_data)

PlottingDF <- figure_s5_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, TimeTillBottleneckMean, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, ScaledTimeTillBottleneckMean, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(ScaledTransmissionRate, ScaledTimeTillBottleneckMean) %>%
  summarize(PMax = max(Prevalence),
            PMin = min(Prevalence)) %>%
  filter(ScaledTimeTillBottleneckMean > 0.15)
PlottingDF$ScaledTransmissionRate <- as.factor(PlottingDF$ScaledTransmissionRate)

tiff("./Figures/Figure S5/Figure S5.tiff", units="in", width = 8, height = 5, res=300)
ggplot(data = PlottingDF) +
  ylim(0, 1) +
  geom_ribbon(aes(x = ScaledTimeTillBottleneckMean, 
                  ymin = PMin, 
                  ymax = PMax, 
                  group = ScaledTransmissionRate, 
                  fill = ScaledTransmissionRate), 
              alpha = 0.50) +
  geom_line(aes(x = ScaledTimeTillBottleneckMean, y = PMax, group = ScaledTransmissionRate), 
            linewidth = 1, 
            linetype = "dashed") +
  geom_line(aes(x = ScaledTimeTillBottleneckMean, y = PMin, group = ScaledTransmissionRate), 
            linewidth = 1, 
            linetype = "dashed") +
  xlab("Timesteps Between Bottlenecks") +
  ylab("Parasite Prevalence") +
  labs(fill = "Transmission Rate") +
  theme_minimal() +
  scale_fill_manual(values = c("lightgreen", "yellow", "orange", "red")) +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()


####Figure S6 - Extinction versus variation in bottleneck frequency (across transmission rates)####
figure_s6_00125_data <- read.csv(file = "./output/figure_s6_00125_data.csv", header = TRUE)
figure_s6_0025_data <- read.csv(file = "./output/figure_s6_0025_data.csv", header = TRUE)
figure_s6_005_data <- read.csv(file = "./output/figure_s6_005_data.csv", header = TRUE)
figure_s6_01_data <- read.csv(file = "./output/figure_s6_01_data.csv", header = TRUE)

figure_s6_data <- rbind(figure_s6_00125_data, 
                         figure_s6_0025_data, 
                         figure_s6_005_data, 
                         figure_s6_01_data)



PlottingDF <- figure_s6_data %>%
  select(Rep, Timepoint, S, I, R, TimeTillBottleneckMean, TimeTillBottleneckCV, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(ScaledTimeTillBottleneckMean = TimeTillBottleneckMean / ScalingFactor) %>%
  select(Rep, ScaledTimepoint, S, I, R, ScaledTimeTillBottleneckMean, TimeTillBottleneckCV, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(ScaledTransmissionRate, ScaledTimeTillBottleneckMean, TimeTillBottleneckCV, Rep) %>%
  summarize(ExtinctionOccurred = case_when(min(Prevalence) == 0~TRUE,
                                           min(Prevalence) > 0~FALSE)) %>%
  mutate(TotalReps = max(Rep) + 1) %>% #Since "Rep" starts with 0
  group_by(ScaledTransmissionRate, ScaledTimeTillBottleneckMean, TimeTillBottleneckCV, TotalReps) %>%
  summarize(ExtinctionCount = sum(ExtinctionOccurred == TRUE)) %>%
  mutate(ExtinctionProbability = ExtinctionCount / TotalReps)

#Since the full data is very large, I have included a saved copy of "PlottingDF", the summarized
#data, in the Figures/Figure S6 folder that can be loaded directly
PlottingDF <- read.csv(file = "./Figures/Figure S6/figure_s6_summarized_data.csv", header = TRUE)


tiff("./Figures/Figure S6/Figure S6 Unlabeled.tiff", units="in", width = 6, height = 5, res=300)
ggplot(data = PlottingDF, aes(x = ScaledTimeTillBottleneckMean, y = ExtinctionProbability, 
                              group = TimeTillBottleneckCV, color = TimeTillBottleneckCV)) +
  facet_grid(ScaledTransmissionRate~.) +
  scale_x_continuous(breaks = c(0, 2, 4, 6, 8, 10)) +
  geom_line(linewidth = 1) +
  scale_color_gradient(low = "black", high = "light grey") +
  labs(color = "Coefficient of\nVariation") +
  xlab("Timesteps Between Bottlenecks (Mean)") +
  ylab("Parasite Extinction Probability") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 14),
        axis.title.x = element_text(size = 18, face = "bold"),
        axis.text.y = element_text(size = 12),
        axis.title.y = element_text(size = 18, face = "bold"),
        panel.border = element_rect(linewidth = 1, fill = NA),
        strip.text.y = element_text(size = 14),
        legend.text = element_text(size = 12),
        legend.title = element_text(size = 14, face = "bold"))
dev.off()


####Figure S7 - pmax and pmin across range of bottleneck severity and transmission rates####
figure_s7_000125_data <- read.csv(file = "./output/figure_s7_00125_data.csv", header = TRUE)
figure_s7_0025_data <- read.csv(file = "./output/figure_s7_0025_data.csv", header = TRUE)
figure_s7_005_data <- read.csv(file = "./output/figure_s7_005_data.csv", header = TRUE)
figure_s7_01_data <- read.csv(file = "./output/figure_s7_01_data.csv", header = TRUE)

figure_s7_data <- rbind(figure_s7_000125_data, figure_s7_0025_data, figure_s7_005_data, figure_s7_01_data)

PlottingDF <- figure_s7_data %>%
  select(Timepoint, S, I, R, InitialPrevalence, BottleneckSizeMean, BirthRate, TransmissionRate, CarryingCapacity) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(BottleneckSizeOutOfK = BottleneckSizeMean / CarryingCapacity) %>%
  select(ScaledTimepoint, S, I, R, InitialPrevalence, BottleneckSizeMean, BottleneckSizeOutOfK, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(ScaledTransmissionRate, BottleneckSizeMean, BottleneckSizeOutOfK) %>%
  summarize(PMax = max(Prevalence),
            PMin = min(Prevalence))
PlottingDF$ScaledTransmissionRate <- as.factor(PlottingDF$ScaledTransmissionRate)


tiff("./Figures/Figure S7/Figure S7.tiff", units="in", width = 8, height = 5, res=300)
ggplot(data = PlottingDF) +
  ylim(0, 1) +
  geom_ribbon(aes(x = BottleneckSizeOutOfK, 
                  ymin = PMin, 
                  ymax = PMax, 
                  group = ScaledTransmissionRate, 
                  fill = ScaledTransmissionRate), 
              alpha = 0.50) +
  geom_line(aes(x = BottleneckSizeOutOfK, y = PMax, group = ScaledTransmissionRate), 
            linewidth = 1, 
            linetype = "dashed") +
  geom_line(aes(x = BottleneckSizeOutOfK, y = PMin, group = ScaledTransmissionRate), 
            linewidth = 1, 
            linetype = "dashed") +
  xlab("Bottleneck Severity\n(Proportion of Carrying Capacity Surviving)") +
  ylab("Parasite Prevalence") +
  labs(fill = "Transmission Rate") +
  theme_minimal() +
  scale_fill_manual(values = c("lightgreen", "yellow", "orange", "red")) +
  theme(axis.text.x = element_text(size = 16),
        axis.title.x = element_text(size = 20, face = "bold"),
        axis.text.y = element_text(size = 16),
        axis.title.y = element_text(size = 20, face = "bold"),
        legend.text = element_text(size = 16),
        legend.title = element_text(size = 20, face = "bold"))
dev.off()


####Figure S8 - Extinction versus variation in bottleneck severity (across transmission rates)####
figure_s8_00125_data <- read.csv(file = "./output/figure_s8_00125_data.csv", header = TRUE)
figure_s8_0025_data <- read.csv(file = "./output/figure_s8_0025_data.csv", header = TRUE)
figure_s8_005_data <- read.csv(file = "./output/figure_s8_005_data.csv", header = TRUE)
figure_s8_01_data <- read.csv(file = "./output/figure_s8_01_data.csv", header = TRUE)

figure_s8_data <- rbind(figure_s8_00125_data, 
                        figure_s8_0025_data, 
                        figure_s8_005_data, 
                        figure_s8_01_data)

PlottingDF <- figure_s8_data %>%
  select(Rep, Timepoint, S, I, R, BottleneckSizeMean, BottleneckSizeCV, CarryingCapacity, BirthRate, TransmissionRate) %>%
  mutate(ScalingFactor = 1 / BirthRate) %>%
  mutate(ScaledBirthRate = BirthRate * ScalingFactor) %>%
  mutate(ScaledTransmissionRate = TransmissionRate * ScalingFactor) %>%
  mutate(ScaledTimepoint = Timepoint / ScalingFactor) %>%
  mutate(BottleneckSizeOutOfK = BottleneckSizeMean / CarryingCapacity) %>%
  select(Rep, ScaledTimepoint, S, I, R, BottleneckSizeMean, BottleneckSizeCV, BottleneckSizeOutOfK, ScaledBirthRate, ScaledTransmissionRate, ScalingFactor) %>%
  mutate(Prevalence = I / (S + I + R)) %>%
  group_by(ScaledTransmissionRate, BottleneckSizeMean, BottleneckSizeCV, BottleneckSizeOutOfK, Rep) %>%
  summarize(ExtinctionOccurred = case_when(min(Prevalence) == 0~TRUE,
                                           min(Prevalence) > 0~FALSE)) %>%
  mutate(TotalReps = max(Rep) + 1) %>% #Since "Rep" starts with 0
  group_by(ScaledTransmissionRate, BottleneckSizeMean, BottleneckSizeCV, BottleneckSizeOutOfK, TotalReps) %>%
  summarize(ExtinctionCount = sum(ExtinctionOccurred == TRUE)) %>%
  mutate(ExtinctionProbability = ExtinctionCount / TotalReps)

#Since the full data is very large, I have included a saved copy of "PlottingDF", the summarized
#data, in the Figures/Figure S8 folder that can be loaded directly
PlottingDF <- read.csv(file = "./Figures/Figure S8/figure_s8_summarized_data.csv", header = TRUE)

tiff("./Figures/Figure S8/Figure S8 Unlabeled.tiff", units="in", width = 6, height = 5, res=300)
ggplot(data = PlottingDF, aes(x = BottleneckSizeOutOfK, y = ExtinctionProbability, 
                                 group = BottleneckSizeCV, color = BottleneckSizeCV)) +
  facet_grid(ScaledTransmissionRate~.) +
  geom_line(linewidth = 1) +
  scale_color_gradient(low = "black", high = "light grey") +
  labs(color = "Coefficient of\nVariation") +
  xlab("Mean Bottleneck Severity\n(Proportion of Carrying Capacity)") +
  ylab("Parasite Extinction Probability") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 14),
        axis.title.x = element_text(size = 18, face = "bold"),
        axis.text.y = element_text(size = 12),
        axis.title.y = element_text(size = 18, face = "bold"),
        panel.border = element_rect(linewidth = 1, fill = NA),
        strip.text.y = element_text(size = 14),
        legend.text = element_text(size = 12),
        legend.title = element_text(size = 14, face = "bold"))
dev.off()

