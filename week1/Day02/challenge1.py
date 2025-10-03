sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
# sample_dict["class"]["student"]["marks"]["history"] = 90
history_value = sample_dict["class"]["student"]["marks"]["history"]
print(history_value)
print(sample_dict.keys())