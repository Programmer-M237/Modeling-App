def load_config(self, config_data):
            if config_data["object_id"] == "23":
                self.lineEdit_3.setText(config_data["object_name"])
                self.spin_box.setValue(config_data["nOf"])
                self.spinBox.setValue(config_data["gtform"])
                self.lineEdit_2.setText(config_data["form"])
                self.form_type = config_data["form_type"]
                self.previous_number_of_forms = config_data["prev_nOf"]
                self.direction_matters = self.config_data["direction_matters"]
                self.reflection = config_data["reflection"]
                self.previous_form_type = config_data["prev_form_type"]
                
                if self.direction_matters == True:
                    self.radioButton.setChecked(True)
                elif self.direction_matters == False:
                    self.radioButton_2.setChecked(True)
                    
                if self.reflection == "identical":
                    self.radioButton_3.setChecked(True)
                elif self.reflection == "distinct":
                    self.radioButton_7.setChecked(True)
                
                layout = self.widget.layout()
                self.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
                self.saved_data = config_data["items"]
                for i in range(config_data["nOf"]):
                    row_widget = QWidget()
                    row_layout = QHBoxLayout(row_widget)
                    
                    label = QLabel(f"Item {i + 1}")
                    line_edit = QLineEdit()
                    
                    if i < len(self.saved_data):
                        line_edit.setText(config_data["items"][i])
                    
                    row_layout.addWidget(label)
                    row_layout.addWidget(line_edit)
                
                    layout.addWidget(row_widget)
                    
                    line_edit.textChanged.connect(self.check_entries)
                    
                scrollbar = self.scrollArea.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
            else:
                QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
            self.check_entries()