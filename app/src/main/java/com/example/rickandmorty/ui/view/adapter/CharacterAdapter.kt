package com.example.rickandmorty.ui.view.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import coil.load
import com.example.rickandmorty.data.local.CharacterEntity
import com.example.rickandmorty.databinding.ItemCharacterBinding

class CharacterAdapter(private val onClick: (CharacterEntity) -> Unit) :
    ListAdapter<CharacterEntity, CharacterAdapter.ViewHolder>(DiffCallback) {

    class ViewHolder(private val binding: ItemCharacterBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(item: CharacterEntity, onClick: (CharacterEntity) -> Unit) {
            binding.txtName.text = item.name
            binding.imgCharacter.load(item.image)
            binding.root.setOnClickListener { onClick(item) }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemCharacterBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(getItem(position), onClick)
    }

    object DiffCallback : DiffUtil.ItemCallback<CharacterEntity>() {
        override fun areItemsTheSame(oldItem: CharacterEntity, newItem: CharacterEntity) = oldItem.id == newItem.id
        override fun areContentsTheSame(oldItem: CharacterEntity, newItem: CharacterEntity) = oldItem == newItem
    }
}
